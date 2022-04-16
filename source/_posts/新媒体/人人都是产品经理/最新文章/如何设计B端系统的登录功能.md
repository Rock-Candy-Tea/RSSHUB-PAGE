
---
title: '如何设计B端系统的登录功能'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/GqLBlbgFE8nVpI4mRyLL.jpg'
author: 人人都是产品经理
comments: false
date: Sat, 16 Apr 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/GqLBlbgFE8nVpI4mRyLL.jpg'
---

<div>   
<blockquote><p>编辑导语：B端系统的设计对于各种应用来说都十分重要，本篇文章作者分享了有关如何设计B端系统的登录功能的内容，详细地介绍了整个设计的过程，一起来学习一下，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5397690 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/GqLBlbgFE8nVpI4mRyLL.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>聊下B端系统的登录功能如何设计。</p>
<h2 id="toc-1">一、设计原则</h2>
<p>登录功能，一个系统最初要设计的功能了，登录功能需要区分<strong>对外用户</strong>和<strong>对内用户</strong>，一般对外的需要有注册功能，对内的基本上都是管理员分配的。</p>
<p>同时登录功能需要搭配【用户管理】一起，登录的信息校验都是来源于【用户管理】。</p>
<p>登录功能的设计原则最重要的就是安全性，灵活性次之。</p>
<p>不管是产品设计上的，用户名、密码、验证码等，还是技术设计上的密码加密、身份认证、服务架构、token、cookie等，安全最该考虑。</p>
<p>同时还要考虑集成系统的情况，即有多个系统使用一个登录功能，进入后需要有一个系统导航，点击每个子系统又可以进入。</p>
<h2 id="toc-2">二、整体方案</h2>
<p>新建【用户管理】，维护用户的基本信息，本身需有添加功能，登录功能的用户数据就来源于此。</p>
<p>登录功能这边需要有用户名、密码和验证码，登录后数据与【用户管理】校验，成功即可进入系统。</p>
<p>有多个系统使用一个登录功能，进入后到系统导航，点击每个子系统又可以进入，登录可保持24h有效，子系统4h有效。</p>
<p>注册功能填写的数据，需要同步到【用户管理】，包括重置密码这些也需要更改【用户管理】的信息。</p>
<h2 id="toc-3">三、原型图</h2>
<p>【用户管理】比较简单，这里只放个注册和登录的界面。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【干货】如何设计B端系统的登录功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/BSscSKt9nOJZVXdxdTw6.png" alt="【干货】如何设计B端系统的登录功能" width="318" height="294" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【干货】如何设计B端系统的登录功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/nnKT1D50fvMlkkM1yMtM.png" alt="【干货】如何设计B端系统的登录功能" width="314" height="391" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、用户管理子段取值逻辑</h2>
<p>【用户管理】的新增、编辑这些按钮，不再细聊，前面聊过很多，简单说下字段需要要哪些，及取值来源，取值来源就需要注意两个：</p>
<ul>
<li>一是注册完成需要将数据保存到【用户管理】；</li>
<li>二是重置密码需要更改【用户管理】的密码，当然，如果有个人信息更改的功能，也需要对应更改数据。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/n4LLijgtNDuADDsJrUzy.png" alt width="323" height="293" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、登录功能详情设计</h2>
<p>这是这个设计里面的重中之重了，尤其是涉及到一些校验的，一定要清晰。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/nDgg16cbQ9vuC2HpSIhn.png" alt width="316" height="328" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/h42vVb11E3gmUPAm2zhN.png" alt width="320" height="299" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/jY1fRWTF6J76LnSH9EWx.png" alt width="319" height="265" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、子系统登录说明</h2>
<p>我们按一个统一登录的设计，进入主体界面后，需要进入每个子系统，点击即可，这里也需要每个子系统授权登录，采取同一套登录权限。</p>
<p>如果是一开始就按这种形式开发的框架，就很容易。</p>
<p>如果多个子系统先开发完成，后续再做统一登录功能，这里就需要将所有子系统的用户信息统一，即每个子系统其实也保留一套用户登录信息。</p>
<p>只是这些都跟统一登录的数据一样，这样就可以进入每个子系统时按这个用户去访问这个子系统的用户权限信息，完成登录。</p>
<p> </p>
<p>本文由 @ Jarvan156 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于 CC0 协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5396606" data-author="1104314" data-avatar="https://static.woshipm.com/APP_U_202204_20220416082604_1320.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            