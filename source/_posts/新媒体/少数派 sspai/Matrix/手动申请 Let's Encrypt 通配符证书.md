
---
title: "手动申请 Let's Encrypt 通配符证书"
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2021/04/11/fce2e320ac6fa3d0510a7cbb2d733719.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Sun, 11 Apr 2021 06:49:29 GMT
thumbnail: 'https://cdn.sspai.com/2021/04/11/fce2e320ac6fa3d0510a7cbb2d733719.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-e1f0100a><div class="content wangEditor-txt minHeight" data-v-e1f0100a><p>又到了续SSL的时候，用的是虚拟主机DA面板自带的一键功能，老失败，后来改用的FreeSSL现在又要手机号，考虑到有多台服务器，决定手动申请通配符证书，以后到期重新申请一次就行，不用再担心碰到一些乱七八糟的事情。</p><p>但过程远没那么简单，坑永远都在。。。</p><h2>安装Certbot</h2><p>按<a href="https://certbot.eff.org/instructions">官方的指导文件</a>安装即可，我家庭服务器用的Ubuntu 20.04 LTS，接下来的命令都是在这台机器上运行的。</p><p>参考官方文档的好处是，有些文章的内容已经过期了，比如有些使用certbot-auto这个工具的文章</p><ul><li>Windows: <a href="https://certbot.eff.org/lets-encrypt/windows-other">https://certbot.eff.org/lets-encrypt/windows-other</a></li><li>Ubuntu: <a href="https://certbot.eff.org/lets-encrypt/ubuntufocal-other">https://certbot.eff.org/lets-encrypt/ubuntufocal-other</a></li></ul><h2>使用Certbot的手动模式向Let's Encrypt 申请证书</h2><ul><li>先上手动模式的用户手册：https://certbot.eff.org/docs/using.html#manual</li><li>Certbot帮助文档命令： Cerbot -h All , 该命令会显示所有子命令和选项的说明</li></ul><p>我所使用的命令如下：</p><pre class="language-text-plain"><code>sudo certbot certonly --manual --preferred-challenges=dns-01</code></pre><p><code>certonly</code>是子命令，只申请或续约证书，不安装。让你可以在任意一台联网的PC设备上申请证书，不必是你的服务器</p><p><code>--manual</code> 选项指以交互或Shell脚本的方式提交信息，我没有脚本，默认是交互方式</p><p><code>--preferred-challenges</code> 选项以<a href="https://certbot.eff.org/docs/using.html#plugins">指定域名认证方式</a>，<code>http-01</code>是文件认证，<code>dns-01</code>是DNS解析指定TXT认证，这里用的DNS认证，文件认证没试过，毕竟我的目标是脱离服务器来申请证书</p><p>一般还会加一个选项<code>--server https://acme-staging-v02.api.letsencrypt.org/directory</code>  用以指定Let's Encrypt 服务器目录，但如果你仔细看过Certbot的<a href="https://certbot.eff.org/docs/using.html#changing-the-acme-server">帮助文档</a>，你会发现默认的就是这个服务器，这里可以省略</p><h2>提交信息</h2><p>运行上面的命令后，则进入交互模式，以提交相关信息，先是邮箱</p><pre class="language-text-plain"><code>Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator manual, Installer None
Enter email address (used for urgent renewal and security notices)
 (Enter 'c' to cancel): </code></pre><p>然后是必定要同意的协议</p><pre class="language-text-plain"><code>Please read the Terms of Service at
https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf. You must
agree in order to register with the ACME server. Do you agree?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: </code></pre><p>再然后是一些新闻之类的邮件推送，可以不接受</p><pre class="language-text-plain"><code>Would you be willing, once your first certificate is successfully issued, to
share your email address with the Electronic Frontier Foundation, a founding
partner of the Let's Encrypt project and the non-profit organization that
develops Certbot? We'd like to send you email about our work encrypting the web,
EFF news, campaigns, and ways to support digital freedom.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: N</code></pre><p>输入域名，通配符域名不包含主域名，所以要填上两个，用逗号分隔</p><pre class="language-text-plain"><code>Account registered.
Please enter in your domain name(s) (comma and/or space separated)  (Enter 'c'
to cancel): yywr.net,*.yywr.net</code></pre><h2>通过DNS认证域所有权</h2><p>接下来会给出需要做DNS TXT记录验证的信息，这里需要注意，这里会出现两次<code>Press Enter to Continue</code>，每一次都给出一串TXT验证字符，<strong> 出现第二次的时候一定要等DNS生效再按回车键</strong></p><pre class="language-text-plain"><code>Requesting a certificate for yywr.net and *.yywr.net
Performing the following challenges:
dns-01 challenge for yywr.net
dns-01 challenge for yywr.net

Please deploy a DNS TXT record under the name
_acme-challenge.yywr.net with the following value:

D7jxyoXXXXXXXXXXXXXXXXXXXXXXXXXXXGdncSBDU

Before continuing, verify the record is deployed.

Press Enter to Continue


Please deploy a DNS TXT record under the name
_acme-challenge.yywr.net with the following value:

I8GXXXXXXXXXXXXXXXXXXXXXXXXXXXXc4Y2Z-11lk

Before continuing, verify the record is deployed.
(This must be set up in addition to the previous challenges; do not remove,
replace, or undo the previous challenge tasks yet. Note that you might be
asked to create multiple distinct TXT records with the same name. This is
permitted by DNS standards.)

Press Enter to Continue</code></pre><h3>DNS解析设置</h3><p>接下来就是我被坑的部分了，个人对DNS解析相关的知识有限，不知道是不是因年纪大了，我看到提示后的理解是添加两个名称为<code>_acme-challenge.yywr.net</code> 的TXT记录，值记录分别使用提供的字符串就好，结果一直验证不过</p><p>后来想到是不是不需要后面的域名，而这时刚好看到另一篇文章提到的主机名称为<code>_acme-challenge</code>，改完后很快就能找到记录了</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/04/11/fce2e320ac6fa3d0510a7cbb2d733719.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/04/11/fce2e320ac6fa3d0510a7cbb2d733719.png" referrerpolicy="no-referrer"><figcaption>主机名称是 _acme-challenge ，不要被命令提示给糊弄了</figcaption></figure><p>可以使用下面命令查看DNS解析是否生效，查询的时候就需要名称＋域名了</p><ul><li>Linux: <code>dig -t txt _acme-challenge.yywr.net</code></li><li>Windows:　<code>nslookup -q=txt _acme-challenge.yywr.net</code></li></ul><p>解析生效会返回<strong>ANSWER</strong>信息，未生效的话则没有，踩坑的时候以为是时间不够没生效，愣了睡了个觉起来再试，注意解析记录不要删除</p><pre class="language-text-plain"><code>dig -t TXT _acme-challenge.yywr.net


; <<>> DiG 9.16.1-Ubuntu <<>> -t TXT _acme-challenge.yywr.net
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 60200
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 0


;; QUESTION SECTION:
;_acme-challenge.yywr.net.      IN      TXT


;; ANSWER SECTION:
_acme-challenge.yywr.net. 3600  IN      TXT     "D7jxyoXXXXXXXXXXXXXXXXXXXXXXXXXXXGdncSBDU"
_acme-challenge.yywr.net. 3600  IN      TXT     "I8GXXXXXXXXXXXXXXXXXXXXXXXXXXXXc4Y2Z-11lk"


;; Query time: 200 msec
;; SERVER: fe80::1%2#53(fe80::1%2%2)
;; WHEN: Sun Apr 11 13:48:11 CST 2021
;; MSG SIZE  rcvd: 154</code></pre><h2>获取证书</h2><p>在确认DNS解析生效之后即可以按回车继续提交，失败会有红色文字提示，一般就是DNS解析未成功，成功则返回类似下面的信息</p><pre class="language-text-plain"><code>Waiting for verification...
Cleaning up challenges


IMPORTANT NOTES:




Congratulations! Your certificate and chain have been saved at:
/etc/letsencrypt/live/yywr.net/fullchain.pem
Your key file has been saved at:
/etc/letsencrypt/live/yywr.net/privkey.pem
Your certificate will expire on 2021-07-10. To obtain a new or
tweaked version of this certificate in the future, simply run
certbot again. To non-interactively renew 
all
 of your
certificates, run "certbot renew"




If you like Certbot, please consider supporting our work by:


Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
Donating to EFF:                    https://eff.org/donate-le</code></pre><p>可以从提示中看到，证书密钥相关都保存在 <code>/etc/letsencrypt/live/yywr.net/</code>这个目录下，部署到服务器就好，我用的宝塔和Directadmin面板，直接贴证书内容就好，其它的还没弄过，就不展开说了。</p><h2>关于续期</h2><p>运行命令再来一次即可，完成之后就会发现证书已经延期了，不需要再次部署。</p><p>参考文章：</p><ul><li><a href="https://blog.csdn.net/u012291393/article/details/78768547">https://blog.csdn.net/u012291393/article/details/78768547</a></li><li><a href="https://jingsam.github.io/2018/10/12/lets-encrypt.html">https://jingsam.github.io/2018/10/12/lets-encrypt.html</a></li></ul><p> </p></div><!----></div><div style="border:1px solid transparent;" data-v-e1f0100a></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-e1f0100a><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>1</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>2</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-7353" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E6%89%8B%E5%8A%A8%E7%94%B3%E8%AF%B7%20Let%27s%20Encrypt%20%E9%80%9A%E9%85%8D%E7%AC%A6%E8%AF%81%E4%B9%A6%E3%80%91%E4%B9%8B%E5%89%8D%E5%BC%80%E5%90%AF%E5%85%A8%E7%AB%99SSL%EF%BC%8C%E7%94%A8%E7%9A%84%E6%98%AF%E8%99%9A%E6%8B%9F%E4%B8%BB%E6%9C%BADA%E9%9D%A2%E6%9D%BF%E8%87%AA%E5%B8%A6%E7%9A%84%E4%B8%80%E9%94%AE%E5%8A%9F%E8%83%BD%EF%BC%8C%E5%90%8E%E6%9D%A5%E5%87%BA%E8%80%81%E5%A4%B1%E8%B4%A5%EF%BC%8C%E6%94%B9%E7%94%A8%E7%9A%84FreeSSL%E7%8E%B0%E5%9C%A8%E5%8F%88%E8%A6%81%E6%89%8B%E6%9C%BA%E5%8F%B7%EF%BC%8C%E8%80%83%E8%99%91%E5%88%B0%E6%9C%89%E5%A4%9A%E5%8F%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%8C%E5%86%B3%E5%AE%9A%E6%89%8B%E5%8A%A8%E7%94%B3%E8%AF%B7%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2021%2F04%2F11%2Fbd43e6fb84afa3ff9499c2781c7d650a.png%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="icon icon-article_weibo right-16"></i></a><span><div role="tooltip" id="el-popover-7236" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><i class="icon icon-article_weixin right-16"></i></span><a href="https://twitter.com/share?text=%E3%80%90%E6%89%8B%E5%8A%A8%E7%94%B3%E8%AF%B7%20Let%27s%20Encrypt%20%E9%80%9A%E9%85%8D%E7%AC%A6%E8%AF%81%E4%B9%A6%E3%80%91%E4%B9%8B%E5%89%8D%E5%BC%80%E5%90%AF%E5%85%A8%E7%AB%99SSL%EF%BC%8C%E7%94%A8%E7%9A%84%E6%98%AF%E8%99%9A%E6%8B%9F%E4%B8%BB%E6%9C%BADA%E9%9D%A2%E6%9D%BF%E8%87%AA%E5%B8%A6%E7%9A%84%E4%B8%80%E9%94%AE%E5%8A%9F%E8%83%BD%EF%BC%8C%E5%90%8E%E6%9D%A5%E5%87%BA%E8%80%81%E5%A4%B1%E8%B4%A5%EF%BC%8C%E6%94%B9%E7%94%A8%E7%9A%84FreeSSL%E7%8E%B0%E5%9C%A8%E5%8F%88%E8%A6%81%E6%89%8B%E6%9C%BA%E5%8F%B7%EF%BC%8C%E8%80%83%E8%99%91%E5%88%B0%E6%9C%89%E5%A4%9A%E5%8F%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%8C%E5%86%B3%E5%AE%9A%E6%89%8B%E5%8A%A8%E7%94%B3%E8%AF%B7%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="icon icon-article_twitter right-16"></i></a></div></div><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            