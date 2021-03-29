
---
title: 'PRD：用Axure原型展示抖音页面交互逻辑'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/aTIYVwa3QvtkNVnUY9fZ.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 27 Mar 2019 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/aTIYVwa3QvtkNVnUY9fZ.jpg'
---

<div>   
<blockquote><p>本文笔者从四个部分输出此份抖音产品需求文档：产品概述、产品结构图、部分逻辑业务，以及，功能需求与交互。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-2138711 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/aTIYVwa3QvtkNVnUY9fZ.jpg" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>笔者作为一名小白，第一次尝试利用Axure来制作PRD，并且重点尝试将页面交互逻辑直接用Axure原型来展示，可能会存在表达不够详细的问题，希望各位大神提出建议，十分感谢。</p>
<h2 id="toc-1">一、产品概述</h2>
<h3>1. 产品介绍</h3>
<p>抖音，是一款可以拍短视频的音乐创意短视频社交软件，该软件于2016年9月上线，是一个专注年轻人音乐短视频社区平台。用户可以通过这款软件选择歌曲，拍摄音乐短视频，形成自己的作品。</p>
<h3>2. 产品需求定位</h3>
<p><strong>产品定位：</strong>适合年轻人的音乐短视频社区，UGC类资讯产品</p>
<p><strong>slogan：</strong>纪录美好生活</p>
<p><strong>用户：</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/4AxYsAFlKkunwDUImxyj.png" alt width="830" height="576" referrerpolicy="no-referrer"></p>
<p>从性别来看，抖音提供的内容对男性与女性拥有同样的吸引力，从年龄段可以看出抖音的目标人群并没有偏离原始目标用户“年轻人”这一群体。</p>
<p><strong>需求整理：</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/rypT6kY6Rw1th6CU3Vct.png" alt width="781" height="440" referrerpolicy="no-referrer"></p>
<p><strong>需求定位脑图展示：</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/jH5GSbvf2Z8WZPTirIwg.png" alt width="663" height="775" referrerpolicy="no-referrer"></p>
<p>这里将产品定位、目标用户、以及需求整理通过思维导图的形式合并展现，个人觉得这样会将结构展示得更加清晰。</p>
<h3>3. 文档属性</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/62N9TxDTSEyGhaJwLZqP.png" alt width="624" height="231" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、版本信息</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/fqa5Ve5NuWoa29dwaeiZ.png" alt width="745" height="1819" referrerpolicy="no-referrer"></p>
<p>抖音主要功能大部分早已完善，版本更新多为细节的优化与一些小功能更新。</p>
<h2 id="toc-3">三、产品结构图</h2>
<h3>1. 产品功能结构图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/2U7BfNo2G86wPSWk3TMp.png" alt width="627" height="1794" referrerpolicy="no-referrer"></p>
<h3>2. 产品信息架构图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/p23C3rrWZf2MYoJMLDGn.png" alt width="1130" height="2263" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、全局说明</h2>
<h3>1. 功能权限</h3>
<p><strong>登录后：</strong>享受APP一切服务。</p>
<p><strong>登陆前：</strong>可以以游客的身份进行浏览，但是不能够使用点赞，评论等对内容进行评判的功能，也无法发布内容。一旦使用这些功能，就会弹出登录界面提示用户登录后才可以使用。</p>
<h3>2. 键盘交互说明</h3>
<p>输入框为手机号或验证码输入框时：弹出数字键盘。</p>
<p>其余输入框：弹出字母全键盘。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/QMuBYFzYWITZaHsxPwci.png" alt width="599" height="550" referrerpolicy="no-referrer"></p>
<h3>3. 页面内交互</h3>
<p><strong>3.1 网络环境：</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/MYNC2kmNWgGbw7O6Xdh3.png" alt width="657" height="592" referrerpolicy="no-referrer"></p>
<p><strong>3.2 加载中：</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/DqGHFZ7Xsyp2D4CRNtpt.png" alt width="336" height="633" referrerpolicy="no-referrer"></p>
<p><strong>3.3 提示：</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/rQjq4lMCZ4LiBFWLaSkn.png" alt width="348" height="639" referrerpolicy="no-referrer"></p>
<p><strong>3.4 首页交互方式：</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/zsYz8ZKrcsKcloHqh60Z.png" alt width="763" height="363" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、部分业务逻辑</h2>
<h3>1. 登录业务逻辑</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/kM7d4OQotdTYl6simNsZ.png" alt width="758" height="580" referrerpolicy="no-referrer"></p>
<h3>2. 观看视频业务逻辑</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/pJgSSpiXyJ1gHVc3E5nI.png" alt width="447" height="765" referrerpolicy="no-referrer"></p>
<h3>3. 制作视频业务逻辑</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/YPhKpaQYYaRltzuA5RyM.png" alt width="784" height="1913" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、核心功能需求与交互</h2>
<p>（逻辑交互部分放到了Axure中，请放大网页比例进行观看）</p>
<h3>1. 总体页面流程图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/8vaDLqRR1Dux0adXY6K1.png" alt width="862" height="932" referrerpolicy="no-referrer"></p>
<h3>2. 登录页面</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/SBJlNOgnSHbjQGJAANEf.png" alt width="702" height="460" referrerpolicy="no-referrer"></p>
<p><strong>功能：</strong>登录</p>
<p><strong>用户场景：</strong></p>
<ul>
<li>想查看自己关注的用户有没有发布新的视频。</li>
<li>想拍摄视频。</li>
<li>想评论视频等。</li>
</ul>
<p><strong>入口：</strong></p>
<ol>
<li>登录</li>
<li>评论，收藏，点赞</li>
<li>拍摄、发布视频</li>
</ol>
<p><strong>前置条件：</strong>用户未登录时，尝试进行须识别个人身份的操作。</p>
<p><strong>优先级：</strong>高</p>
<p><strong>页面说明：</strong></p>
<ul>
<li>手机号默认+86，输入限制11位，密码输入不可见，密码必须高于6位。</li>
<li>当输入非数字内容时，输入界面不显示任何内容；输入数字小于11位时，点击登录提示“请输入11位数字手机号”当输入大于11位数字时，超过部分不显示。</li>
<li>获取验证码后，按钮内容变为“60s”并降低灰度开始60秒倒数，60秒后按钮内容变为“点击重新获取”，恢复原来的灰度。</li>
<li>忘记密码时，可点击“忘记密码”跳转到找回密码页面，输入登录名后滑动滑块验证获取验证码，输入验证码后点击下一步进行密码重置。</li>
</ul>
<p><strong>交互逻辑：</strong>如图。</p>
<h3>3. 推荐短视频页面</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/DTHyxOZP56sFyAgtPK0a.png" alt width="1010" height="806" referrerpolicy="no-referrer"></p>
<p><strong>功能：</strong>推荐短视频观看。</p>
<p><strong>用户场景：</strong>想观看自己喜欢的短视频。</p>
<p><strong>页面说明：</strong></p>
<ul>
<li>未登录不能参与评论、转发、收藏等操作，进行相应操作时跳转至登录界面。</li>
<li>评论时键盘从下方弹出。</li>
<li>评论字数最大不能超过110字，超过是给出提示。</li>
</ul>
<p><strong>入口：</strong>首页</p>
<p><strong>前置条件：</strong>无</p>
<p><strong>优先级：</strong>高</p>
<p><strong>交互逻辑：</strong>如图</p>
<h3>4. 附近短视频页面</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/suci9LzNO5Gd8brbZzXs.png" alt width="4331" height="4000" referrerpolicy="no-referrer"></p>
<p><strong>功能：</strong>附近短视频观看。</p>
<p><strong>用户场景：</strong>看看附近有没有什么人拍摄了短视频。</p>
<p><strong>页面说明：</strong></p>
<ul>
<li>未登录不能参与评论、转发、收藏等操作，进行相应操作时跳转至登录界面。</li>
<li>评论时键盘从下方弹出。</li>
<li>评论字数最大不能超过110字，超过是给出提示。</li>
</ul>
<p><strong>入口：</strong>点击“附近”</p>
<p><strong>前置条件：</strong>无</p>
<p><strong>优先级：</strong>高</p>
<p><strong>交互逻辑：</strong>如图</p>
<h3>5. 关注的短视频页面</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/snbAxu3auUn5SUvvZH5f.png" alt width="3150" height="4000" referrerpolicy="no-referrer"></p>
<p><strong>功能：</strong>关注的短视频观看</p>
<p><strong>用户场景：</strong>看看自己关注的用户有没有更新内容。</p>
<p><strong>页面说明：</strong></p>
<ul>
<li>未登录不能参与评论、转发、收藏等操作，进行相应操作时跳转至登录界面。</li>
<li>评论时键盘从下方弹出。</li>
<li>评论字数最大不能超过110字，超过是给出提示。</li>
</ul>
<p><strong>入口：</strong>1.点击“关注”；2.点击“我的”-》“关注”</p>
<p><strong>前置条件：</strong>登录</p>
<p><strong>优先级：</strong>高</p>
<p><strong>交互逻辑：</strong>如图</p>
<h3>6. 拍摄短视频页面</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/xa8AlVsDJiZYz7OWsF3h.png" alt width="4403" height="3988" referrerpolicy="no-referrer"></p>
<p><strong>功能：</strong>拍摄视频</p>
<p><strong>用户场景：</strong>用户想自己拍摄短视频。</p>
<p><strong>页面说明：</strong></p>
<ul>
<li>拍摄方式可在长按拍与单机拍之间转换，转换方式如图。</li>
<li>左上角“X”可退出拍摄界面。</li>
</ul>
<p><strong>入口：</strong></p>
<ol>
<li>在首页进行屏幕右滑</li>
<li>点击首页“+”号</li>
</ol>
<p><strong>前置条件：</strong>登录</p>
<p><strong>优先级：</strong>高</p>
<p><strong>交互逻辑：</strong>如图</p>
<h3>7. 编辑短视频页面</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/I24SFhJ1pnCZsQSHvcrT.png" alt width="1507" height="738" referrerpolicy="no-referrer"></p>
<p><strong>功能：</strong>编辑视频</p>
<p><strong>用户场景：</strong>用户在拍摄短视频需要对视频进行编辑，包括音乐剪辑，添加特效等操作。</p>
<p><strong>页面说明：</strong></p>
<ul>
<li>该部分添加的滤镜，特效与道具与拍摄阶段提供的一致。</li>
<li>左上角“<”可返回到拍摄界面。</li>
</ul>
<p><strong>入口：</strong>拍摄视频完成后</p>
<p><strong>前置条件：</strong>拍摄视频</p>
<p><strong>优先级：</strong>高</p>
<p><strong>交互逻辑：</strong>如图</p>
<h3>8. 发布视频页面</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/03/Ni7AQ7uReyNGm2STl6uB.png" alt width="2861" height="4078" referrerpolicy="no-referrer"></p>
<p><strong>功能：</strong>发布视频</p>
<p><strong>用户场景：</strong>用户在编辑短视频后需要发布视频，添加相关活动，地理位置等。</p>
<p><strong>页面说明：</strong></p>
<ul>
<li>发布内容字数不能超过80字。</li>
<li>添加位置中，搜索地址以后只能在下方菜单中选择一个相近地点。</li>
</ul>
<p><strong>入口：</strong>编辑视频完成后。</p>
<p><strong>前置条件：</strong>编辑视频</p>
<p><strong>优先级：</strong>高</p>
<p><strong>交互逻辑：</strong>如图</p>
<h2 id="toc-7">七、小结</h2>
<p>整个抖音的功能结构比较繁杂，本文只选取了部分核心功能进行需求描写，由于交互都写在了Axure里，可能会有一些情况没有考虑到，还请大神轻喷。另外本文章节结构的思路参考了@神户短郎<a href="http://www.woshipm.com/it/950565.html" target="_blank" rel="noopener">《用Axure写PRD：虎扑app产品需求文档》</a></p>
<p> </p>
<p>本文由@Kazan 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Unsplash, 基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="2124535" data-author="335983" data-avatar="http://image.woshipm.com/wp-files/2019/03/ljbHOog9mbomwbbKGw2K.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            