
---
title: 'Chrome开发者工具详解（上）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e13ecd6d5c2b42cba30291236d59a9ff~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 06 May 2021 01:10:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e13ecd6d5c2b42cba30291236d59a9ff~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">简介</h1>
<p>浏览器自带的工具，用于开发时调试和检查网页应用的状态</p>
<h1 data-id="heading-1">打开方式</h1>
<ul>
<li>chrome 右上角菜单，更多工具，开发者工具</li>
<li>页面上右键，菜单里选检查（inspect）</li>
<li>windows：ctrl + shift + I （或者 F12）</li>
<li>mac： cmd + opt + I</li>
</ul>
<h1 data-id="heading-2">element 面板</h1>
<p>element 面板支持查找网页源代码HTML中的任一元素,手动修改任一元素的属性和样式且能实时在浏览器里面得到反馈。如下图所示：element 面板由左边<strong>DOM元素面板</strong>和右边<strong>属性面板</strong>组成</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e13ecd6d5c2b42cba30291236d59a9ff~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">DOM元素面板</h2>
<h3 data-id="heading-4">查看 DOM 元素在页面上的对应显示（可结合面板上鼠标一起用）</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f134639b3354524bed082e99dd86dd2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">搜索 DOM 元素(选中面板ctrl + F)</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/930f92eaa0914f62ac6bdd1243b87be8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">添加删除和修改元素</h3>
<p>可直接在DOM元素面板上增加DOM元素或删除DOM元素
右键点击Edit as HTML这样你就可以愉快的操作DOM元素啦~
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b4c6fe105c94c88bd6e43e92a2914c9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4db3f6f18a77482cb9fc3b9cb6a127f0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">添加伪类</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8a652ff6c12488dba7c3f29ae7ffcf4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">拖动 DOM 元素来修改位置</h3>
<p>可以像平时拖动文件夹一样拖到DOM元素，并修改DOM元素的位置</p>
<h3 data-id="heading-9">选中节点时通过 $0 就可以引用到该节点</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/edd95aaca6a3420d837766b25c3d7a60~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">scroll into view 定位节点</h3>
<p>右键点击scroll inti view页面就会滚动到目标位置啦~
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1292a3bcae844e8bc03b53bf6907725~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">属性面板</h2>
<h3 data-id="heading-12">style面板</h3>
<ul>
<li>修改样式</li>
<li>toggle 样式</li>
<li>伪类调试(调试元素伪类对应的样式)
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2614675361df4a7d81e3f83e2af2eba2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>新增类
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7faae4d7de9d4d5cb23f87973f0bcd60~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
<h3 data-id="heading-13">computed面板</h3>
<ul>
<li>查看样式</li>
<li>调试盒模型</li>
<li>定位样式生效的位置</li>
<li>对css属性进行分组</li>
</ul>
<h1 data-id="heading-14">animations</h1>
<p>动画检查器</p>
<h2 data-id="heading-15">作用：</h2>
<ul>
<li>检查动画。放慢，重放或检查动画组的源代码。</li>
<li>修改动画。修改动画组的时间，延迟，持续时间或关键帧偏移。</li>
</ul>
<h2 data-id="heading-16">如何打开animations面板</h2>
<ul>
<li>
<p>单击更多打开主菜单->导航到“更多工具”子菜单->选择Animations
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e64596ea8c954ddeaf90c116f444a21b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>打开命令菜单（快捷键Ctrl + Shift + P），然后键入Show Animations。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f1d4742867a47f3abb27b995acca140~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>animations面板所在位置
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f9c864d2c074fcebb69dabf342a3420~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h2 data-id="heading-17">面板详解</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f017c35d50934ca6907e758c94cab832~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>1：控件面板。清除所有当前捕获的动画组，或更改当前所选动画组的速度。</li>
<li>2：概述面板。在此处选择一个动画组以在“详细信息。检查并修改当前选定的动画组”窗格中进行检查和修改</li>
<li>3：时间轴面板。从此处暂停并开始动画，或跳到动画中的特定点
<img width="800" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2dd22735c694cb3adebe0cd33255d7e~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer"></li>
<li>4：详细信息。检查并修改当前选定的动画组
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59b9a5b915f44f02a8816e3c7aee9759~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
<h2 data-id="heading-18">控件面板</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27815e69616c41b0ae78a72079c7a1ea~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>1：清除已经捕获到的动画</li>
<li>2：暂停/启动 动画的播放</li>
<li>3：修改动画的播放速度</li>
</ul>
<h2 data-id="heading-19">概述面板 and 详细信息面板</h2>
<ul>
<li>
<p>捕获动画组后，在“概述”面板中单击它以查看其详细信息。在“详细信息”面板中，每个单独的动画都有其自己的行。</p>
</li>
<li>
<p>将鼠标悬停在动画上以在视口中突出显示它。单击动画以在“元素”面板中将其选中。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23cda118787d4095883ba8ac6541c1dc~tplv-k3u1fbpfcp-watermark.image" width="800" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>动画的最左边，颜色较深的部分是它的定义。向右，更浅色部分代表迭代。例如，在下面的截图中，第二部分和第三部分代表第一部分的迭代。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34460de3037943ccbb2158c202aef21e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>若要更改动画的持续时间，单击并拖动第一个或最后一个圆圈。</p>
</li>
</ul>
<h1 data-id="heading-20">NetWork 面板</h1>
<p>NetWork面板主要用来检查网络活动</p>
<h2 data-id="heading-21">网络日志</h2>
<p>网络日志的每一行代表一个资源。默认情况下，资源按时间顺序列出。最重要的资源通常是主要的HTML文档。最底层的资源是最后请求的资源。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f65b19cc2324f80bb32d6fb5f4ea6c6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-22">默认列</h3>
<ul>
<li>Name：资源请求url(从哪里请求资源)</li>
<li>Status：HTTP响应码</li>
<li>Type：资源类型</li>
<li>Initiator：是什么导致了资源的请求。单击“Initiator”列中的链接，将您带到引起请求的源代码。</li>
<li>Time：请求花了多长时间</li>
<li>Waterfall：请求不同阶段的图形表示。将鼠标悬停在瀑布上可以查看细目。</li>
</ul>
<h3 data-id="heading-23">网络日志的列是可配置的。您可以右键单击表头隐藏/显示列</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31aeca6bb73f4f40a6e3db5a20c5bdac~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-24">模拟一个较慢的网络连接</h2>
<p>个别情况下我们需要模拟一个网络较差的环境来测试我们的网站是否会出现异常情况。具体操作如下：</p>
<ul>
<li>
<p>Throttling菜单选中Slow 3G</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fc1c1b2734049ff9ce5f200b80e2411~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>当您想了解首次访问者如何体验页面加载时，长按Reload 重装，然后选择Empty Cache And Hard Reload。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36b9a40a63cb4db5844f658098880e54~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h2 data-id="heading-25">Capture screenshots</h2>
<p>Capture screenshots使您可以看到页面在加载过程中的外观，屏幕截图窗格提供了缩略图的缩略图，该缩略图显示了页面在加载过程中各个点的外观。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3887329efa094350a4324dff278c0171~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>单击任意一个缩略图。DevTools会向您显示当时正在发生的网络活动。</p>
</li>
<li>
<p>双击缩略图，得到缩略图录像，点击前进后退按钮可以查看不同时间点的页面活动</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a361d2c5b5644f9bbba32ff7420b144a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h2 data-id="heading-26">Filter resources</h2>
<ul>
<li>
<p>单击过滤器筛选显示它。在过滤器输入目标资源或点击右边的资源类型按钮进行过滤。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e7cb6600c414b338af655539f3d29ab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h2 data-id="heading-27">Block requests</h2>
<p>当我们想测试页面的某些资源不可用时，页面的外观和行为如何？它会完全失败，还是仍然有些功能？Block requests 可以实现这个效果</p>
<ul>
<li>
<p>按Control + Shift + P或Command + Shift + P（Mac）打开“命令菜单”。</p>
</li>
<li>
<p>键入block，选择显示请求阻止，然后按Enter。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d982b96e1fd542158de31bdd45fdc157~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>点击添加模式 +</p>
</li>
<li>
<p>输入main.css，点击添加</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44078bcdc59b4165b9e65a9413f842de~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>重新加载页面。正如预期的那样，页面的样式有些混乱，因为其主要样式表已被阻止。请注意main.css网络日志中的行。红色文本表示该资源已被阻止。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a1317ce163d4724a1dba8abab44d3ca~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h1 data-id="heading-28">最后</h1>
<p>感谢大家阅读，如有问题欢迎纠正！</p></div>  
</div>
            