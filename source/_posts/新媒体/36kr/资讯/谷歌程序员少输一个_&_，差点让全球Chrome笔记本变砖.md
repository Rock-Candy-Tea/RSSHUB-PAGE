
---
title: '谷歌程序员少输一个_&_，差点让全球Chrome笔记本变砖'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210726/v2_02c0f1f2bad948db9ae4ce83f7f9d1b6_img_000'
author: 36kr
comments: false
date: Mon, 26 Jul 2021 07:45:03 GMT
thumbnail: 'https://img.36krcdn.com/20210726/v2_02c0f1f2bad948db9ae4ce83f7f9d1b6_img_000'
---

<div>   
<p>代码只是少了一个字符，后果竟如此可怕。</p> 
<p>上周，一些使用Chrome OS笔记本的用户发现，一旦重启笔记本，就将陷入了无法登录的死循环。</p> 
<p><img src="https://img.36krcdn.com/20210726/v2_02c0f1f2bad948db9ae4ce83f7f9d1b6_img_000" data-img-size-val="1080,728" referrerpolicy="no-referrer"></p> 
<p>明明输入的开机密码是对的，但就是一直提示“无法验证您的密码”，进不了系统。更严重的情况是笔记本将反复重启。</p> 
<p>一台好好的笔记本怎么突然就“变砖”了呢？</p> 
<p>原来都是Chrome OS一次悄悄自动更新惹的祸。</p> 
<p>由于ChromeOS是开源的，一位Reddit网友仔细检查系统更新的代码，发现其中的低级错误令人哭笑不得。</p> 
<p><img src="https://img.36krcdn.com/20210726/v2_da36fb2e5f274dbca75dd165f14593b7_img_000" data-img-size-val="980,317" referrerpolicy="no-referrer"></p> 
<h2>少一个“&”惹的祸</h2> 
<p>这位网友仔细对比两份代码后发现，这个“惊天大bug”背后竟然只是<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>程序员少输了一个字符“&”。</p> 
<p>原本正确的代码应该是：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>if (keydata.hasvalue() && !key_data->label().empty())</p></li> 
</ul> 
<p>而这位程序员却把这句if语句写成了</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>if (keydata.hasvalue() & !key_data->label().empty())</p></li> 
</ul> 
<p>“&&”和“&”两个运算符虽然看起来只差一点点，但二者作用真是天壤之别。</p> 
<p>前者是对两个变量求“与”（AND），而后者是对这两个值按位求与。</p> 
<p>这样就导致了条件语句两边变量每一位都会被求与，即使has_value()为真，返回结果也不一定就是真。</p> 
<p>而这串代码是Chrome OS中保存用户加密密钥的部分，由于这个错误，系统无法验证将存储的密钥与输入密码进行比较，就出现了尴尬的一幕。</p> 
<p>接到用户的反馈后，谷歌迅速发布了91.0.4472.167更新来解决该问题。</p> 
<p>如果你的Chrome笔记本只是无法进入当前账户，那么可以先尝试安装最新更新，而不会丢失文件。</p> 
<p>如果你的笔记本无限重启，就只能回复出厂设置然后再接收更新了，数据也会全部丢失。</p> 
<h2>没测试就发布，着实离谱</h2> 
<p>堂堂互联网大厂竟犯如此低级错误，这令不少Chromebook用户感到愤怒：</p> 
<blockquote> 
 <p>谷歌的测试团队这两个月是休假了吗？</p> 
</blockquote> 
<p><img src="https://img.36krcdn.com/20210726/v2_01906cacc09f48e084b4a63136d31978_img_000" data-img-size-val="1080,260" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p>谷歌没有代码测试的吗？为什么会在没有测试的情况下把代码发布到生产环境。</p> 
</blockquote> 
<p><img src="https://img.36krcdn.com/20210726/v2_981fb5b1269847f6aa0bc364e45ef621_img_000" data-img-size-val="1080,244" referrerpolicy="no-referrer"></p> 
<p>Chrome OS过去一直“小错不断”，所以有些用户已经学得精明了：</p> 
<blockquote> 
 <p>我已经学会了等更新发布一段时间后再升级。</p> 
</blockquote> 
<p><img src="https://img.36krcdn.com/20210726/v2_5a9704e752664c16acb32369c473a6e4_img_000" data-img-size-val="1080,198" referrerpolicy="no-referrer"></p> 
<p>真是没想到，代码少一个字符竟有这么大的破坏力。好在Chrome OS系统更新是分批进行，波及面也不算太广。</p> 
<p>看到这个谷歌程序员的bug，你有没有想起自己犯过哪些低级错误呢？（比如把等于号“==”写成了赋值号“=”）</p> 
<h3 label="二级标题">参考链接：</h3> 
<p>[1]https://9to5google.com/2021/07/21/psa-chrome-os-update-locking-out-accounts/</p> 
<p>[2]https://arstechnica.com/gadgets/2021/07/google-pushed-a-one-character-typo-to-production-bricking-chrome-os-devices/?comments=1</p> 
<p>[3]https://www.reddit.com/r/chromeos/comments/onlcus/update_it_seems_google_has_pulled_the_165_stable/h5vev76/</p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/z3jlnvxdfhg_Ppb-o_fkKQ">“量子位”（ID:QbitAI）</a>，作者：晓查，36氪经授权发布。</p>  
</div>
            