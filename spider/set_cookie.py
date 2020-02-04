from urllib import request


def main():
    my_profile = 'https://user.qzone.qq.com/269524963'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        # 设置cookie保持登录状态
        # 'cookie':'pgv_pvi=8412289024; RK=jLhMzt3Cdx; ptcz=a8defb095fe0d097a6d1a28441745a7a1ff6f2022e7e365f5e1b47cf2b539687; pgv_pvid=6362010689; Loading=Yes; __Q_w_s__QZN_TodoMsgCnt=1; pgv_si=s1881634816; _qpsvr_localtk=0.2646905587170174; zzpaneluin=; zzpanelkey=; uin=o0269524963; skey=@p6zziRwc1; p_uin=o0269524963; pt4_token=y4XiTWk57yYf9d3kQGN3cew*DFOFDMS-e-txx6qIurI_; p_skey=FTi7LaKSKfgaLHg5lmlRI3C4Qgh1kSSmiCNABSgv8us_; pgv_info=ssid=s2320362009'
        }
    req = request.Request(url=my_profile, headers=headers)
    res = request.urlopen(req)
    content = res.read()
    with open('login.html', 'wb') as f:
        f.write(content)


if __name__ == '__main__':
    main()
