import os
import multiprocessing


def copy_file(file_name, old_folder_name, new_folder_name, queue):
    with open(old_folder_name + '/' + file_name, 'rb') as old_file:
        content = old_file.read()
    with open(new_folder_name + '/' + file_name, 'wb') as new_file:
        new_file.write(content)
    queue.put(file_name)


def main():
    old_folder_name = input("输入需要copy的文件夹名：")
    try:
        new_folder_name = 'new_' + old_folder_name
        os.mkdir(new_folder_name)
    except:
        pass
    file_names = os.listdir(old_folder_name)  # 返回list
    files_num = len(file_names)
    copied_file = 0
    pool = multiprocessing.Pool(2)
    queue = multiprocessing.Manager().Queue()

    for file_name in file_names:
        # 在进程执行过程中若产生异常，不会显示异常信息
        pool.apply_async(copy_file, args=(file_name, old_folder_name, new_folder_name, queue))
    pool.close()
    while True:
        queue.get()
        copied_file += 1
        # 完成打印不换行，且回到本行行首
        print("\r完成进度为：%.2f %%" % (copied_file / files_num * 100), end="")
        if copied_file == files_num:
            break
    pool.join()


if __name__ == '__main__':
    main()
