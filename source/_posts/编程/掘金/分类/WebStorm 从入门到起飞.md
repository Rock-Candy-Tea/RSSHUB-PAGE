
---
title: 'WebStorm 从入门到起飞'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77b821e947c24251bcb49a22aeb47c22~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 18 Jun 2021 22:46:39 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77b821e947c24251bcb49a22aeb47c22~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAAQlBMVEVHcEwlRnqtZBj76q4lRnolRnolRnolRnolRnokRnr/gGtrVUeLXDBKTl+hYSHasW7Ik0zs0JG4dCvUdEE0SW+rYxrLQJfjAAAACnRSTlMA////0H/xUaMi5MCoTwAACfVJREFUeNrtnQl3qygUgJ9GXAqosfL//+pgmgXwXmRNJGdu55xO+6rx8+6I8O9fehmGriN93zdN07bVXdpW/ih/SbpuGP6dXbpOXv7z2i3S9ISck2eQOnAhMHG64VQQbmrAaM4B05GmipaGdB+m6BNQPBXzMYtKR3EPbB/RS5eY4g+lIW9WBqnySCvVMrzRpqqs0g9nwVg5p1KYlHEchRT5bftp+y3n6xlQDjAkABtrKULU9f377ev+4/1/NiT+URRiZRhrcZP6WLa/Gq005BORaqXsdYEuHPIP798ZxSyt6d5sVfxJESRCsvB32lfXwhRjnUBGmKXNoJQe04VIASJqRC/9G7yDsyQMiloYz+0pHYghEoPISAGgpDSvHsCoMwmA0mfjSG5UOsqah2RodkljzMkhZZdamiEDB8+Nsbk9T04yGNljDXGOZZ6u0+Tj9DuvbyNJBuPO0ABtLNPlJtfZJ4CNNCWJoY8gddwxNpm9YrHh9DEkBoeMud4Kma8XRZaYpBJOYvg59U9wOsblMvmGrzQe30dyqFZ1dxPfO0FT5BOdw989THVs4q1TFk+iN4PMu7CaLpd4EJOExNaJLE4d0xQKYpJ0cY5Ozcwwu6WOu2cs9TUYxPB4b4fvLRzTUXbT1HH7y0BnB0j6CAehkPFfFzd1TMsi6sU1/P4VM9NiISHBlYnBMR+kad075sXlmMehj1twnfTUqJH4GJfqIKte7S72emPnHbdiYHIB0e6ATjKq1UoTaFh6wBL2csMIVo9fH/v6QRHAgoxrOHQQxG/36tC1ODmGOeBGBRmXalgcdhDQ1xF1vI6a3DF2d4r7G1enOUgNOshlFq7qUCxrca9ldiCam7ilxRbP6JbOYsYtfLFmkcXEgLG1DN/6eroxHjqh5bh+Uw27e1oWVK7pN+AqwzUcq/UYTPw8nWufLFBHN2zcxLRYlmGPs6rA2Wy0uJe/E7TknbHIa1WH1bLA8DAj3JpxET+FCNCWZ5uNT6jxTPZK/1mXoCBeKlGLRT2lP69XN3XdqqCojKX1ZVda6iD2McjeXSHa0I+AHd2InGAJgjRVM6gOBfygDrarRJnho6eQBbrns+HkcNUCWtYClJa66qFgPbqqZEBTCOAgRqxCOhQBWpZeIC6QBq91hEoI5unTjsMsK9DCFigY9WNn19hgVCrELalrTw6WnYMYzjHhQ2/7G2xTx1HvwpzSe4cVi5ORQQwMW9+72FU5L4gGsa6Yu1RcDeIhs64Qs8izt0vGH+n9/IKaIlYpM2UqkYOrwwq5CgBjWpyGtxaonxe4KaJ3hx+7O0HaqVkxLBPj8FmBVmjNevIUFhUuDmMq5NDV9RwyPe/95IvxAhG7ymqxHGE5sZJL2kPLUhUinkXfrnFwGFwXD99djNLSFh/meXEb2B6Oyiwm0I7BC+OlTlOVPk9K8CIYzu5YHwKDTI6XAo5lz3WEqEXwQRKhh5cyLa6D81P4PXBw984as9YaGXHwx4Ba8rmOldUat/BHt9cQ38AaljnBdCJqs60OcXVDJZP//ZwSWtV9FpHNtgg22KuYx/U2tB5Mcp1TYOiphNhiFjgWeJ3DL2OZpuuUisIoUyzZEJ76I+LmyqWdv8LwnEiwMYczihjxeqtBsuFJSTg2oD1ETQx4v6D1VleSZW1xCwvAfVGWpQ069kgrQksAUW2rReYzsboIjSABuDQX0QJwB9cnZVgWVgE31vrklAJnEmVObykgYCk/VGX5OlpuKb5eiovUAvJ2tMstw0kIkNdpiSA91K6XA6K8CVCyr4PePhTo65q3DyX7OpTbSVk1PB62mhJ9HSpSqtKaESxsFRm0tLBVcvTV+vbBrLRK4hC7aitN9B0ZpX6vNMgjGIt5ZdmMv32KrmprD1afsPd4FEhThK0+WfTl3kpd482AGvG3jQdZK1+t8ireDswhofigRb3fxfI/4jj+xkffUX/1ccxxhEP9qyyBEH9Cx9vhf8TB7eiSpBHjZVSa4whQMJC1TqIR6q8RERtjOr2ID0yx3oYi0oAIvZCPz4eG64p3ObuREeOHUIR3MBVJwq9yll5P7KHdiPBOiOoRa/AjXz21J3k04l+i8OjErj4kaXWQiIVO/EvA+KLRAEnUVomtjPd6SvR3RLoeMT54nKFH1EqtkkEGFaQuTlSQrsxhRiOIt51S/Ho8B11+FUlwRaHnU4utEI38/mgSjRJ8PhWEtN6Z6WcncQOU4efjKoh3zfi7/+DfhPrwOZ9a/iYBiVJJxPlei3CqIDTYEqAPFow5/c71fAdVIwmo4n+cTIGbr2n9NULAE5ifcNNS63hvEOFk0wxYnICBBZ0I9xERBVILF0uggNdxuOkR4S6ngvgPmArzHv4KpMKGQFjQ+Rw6q9dC6R6dgZaJF7RVWIH0BTY9h+fz0ohHOyLuy+He/hN4GUR3/RxcBx2f76izarI9CaXmzRmhNQuSfIgJkva5GzN6HJbhQxCNsDGDSh56plmef6sg2eaXPsYBt5W+H6VE6omG6hOS1w4hiTWiThbJ1YO+RSO1vrpMlomf6nhQGz0m7qT6W04XOUHyzhZ4rkG+0hxL66oDW9mnPWyL3TMmssxyQUwr01CHX7b2OvUIaqS48TnMtAoEQTQixJeAlDfSiGmk/l8jpwIpTyFqOfeNIHWBooC036ERtUQp2tm/CKT5jjySbxTlvUVj2yhjvyWDVL3yfKRojXwLSEWUp7q0PBAKPp7m5YGoT3WH7wAZ1BeOywNZv3Gak/LIqriwxbQ5jaTcsEW1eb+FvoWo+zr5V/IUOvNtsapU2zJXSyj0xVB13sPfq0kkZA7dubIIKXIlJ8Cy7u+BN22RVcr+peOuxHdcBbA04FAVmEoEtO5vX55K4KVZS1QJvBBzU1rgUl8JapBNYIowLoZtD9NWRTWKqqe36L48BSz8QPH9epqqIDehlh2UuqocEmrdV7AvhuRoM74m80yeDIEX3ppreNN235FxV58DNjhswn5K8zK21+5ctjut6NmUIoy9tVvitnHr2VDM3ahtW8KQ/Vbsp9GGiWHfk8skyTSFz9/HdxhHe4uR/RxX/mG1SGXwypcDJNmCMfucZ/C1CuCQUbiBUDYbe7tiRkZX8GIat50d+wqR1fdN7ygGzrHrcN4kGFHK02cil5M6INgQVsvnNz77T5PqUFYJJInYmIBplJfP5On4eiOwYfhuCD44oLyYVs43rI1rk3H7usttzq8Qo3j84vavN9mOkAeuq8dHEd9NtCVKX51Oen+MM6IEYvz5StOehKLpIjD+nKU5AQWJpLizdB+1sb5LQvFRxbSJVGHmSdK/0WWaPguEYmcSJ68aWkK6rAw6jwSSCmrTWVHT96R7HwHANEgqybVJL+E2vE2q7Uu91Gr73SbbNUvZDtiOlCeIv4r/AI+0XUwz1lvcAAAAAElFTkSuQmCC")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>最近发现身边的同事和朋友使用 VsCode 比较多。我自己也去知乎的 <a href="https://www.zhihu.com/question/301095344" target="_blank" rel="nofollow noopener noreferrer">为什么 Webstorm 这么好用还会有人去用 Vscode</a> 调研了一下。发现大家不喜欢 WebStorm 有几个原因：</p>
<ul>
<li>收钱</li>
<li>功能多、杂</li>
<li>笨重</li>
</ul>
<p>我自己在使用 WebStorm 的时候也遇到过这些问题，之后都有了一些解决方法了，今天就给大家分享一下吧。</p>
<h2 data-id="heading-1">如何获取 Jetbrains</h2>
<p>首先还是淘宝大法，下到几块钱，上到十几块钱。无非就是使用注册机生成注册码，要不就是用自己的学生账号给你申请 license。</p>
<p><strong>个人不是很推荐这种方式，一个是体验肯定不会很好，另一个大家都是做开发的，还是有点知识产权意识会比较好。</strong></p>
<p><strong>另一个方法就是靠公司啦，如果公司买了的话，一般会把生成 license 的服务放到自己服务器上，向公司要一个 license server 地址，填入就可以了。</strong> 比如这样：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77b821e947c24251bcb49a22aeb47c22~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>如果你是学生，可以用你的学生账号到 <a href="https://www.jetbrains.com/shop/eform/students" target="_blank" rel="nofollow noopener noreferrer">官方这里</a> 申请 license，有效期为一年。</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7756f6099592421a9fe652d729c99275~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>大家不要觉得一年时间很短，程序员有多少个一年呢？可能 5 年之后已经不再是一线的大头兵了，使用最多的软件反而可能是 Power Point。一年时间足够入门一两个技术并做出项目了，加油吧！</p>
</blockquote>
<p><strong>最后一个方法也是最推荐的方法，就是用你自己的 Github 项目来申请，申请地址在 <a href="https://www.jetbrains.com/shop/eform/opensource" target="_blank" rel="nofollow noopener noreferrer">这里</a>。填好项目信息和个人信息就 OK 了。注意：一定要有 3 个月的提交记录哦。</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f02cbfe60fb456e867d5f0b43004c7b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面两种申请的方法大概 1 到 2 周就会有邮件回复了。</p>
<blockquote>
<p>个人比较推荐的做法是：在 Github 上创建一个 blog 的仓库，每写一篇文章就 commit 到这个仓库里。有几个好处：一个是逼自己多写文章，另一个是可以赚取 Github 的一个绿点，最后就是可以保持这个项目是一直 active 状态的，可以申请 Jetbrains license，一举多得。</p>
</blockquote>
<p>像我自己就有一个：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23f255c1a8d441edb7cc6fa34ffa46fd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">主题 & 字体</h2>
<p>主题和字体应该是大家最关注的东西了，这里强推 Material UI 的 Darker 主题和 Atom Material Icons。</p>
<p>首先 <strong>command + ,</strong> 打开设置，找到 <strong>Plugins</strong>，把 <strong>Material UI</strong> 和 <strong>Atom Material Icons</strong> 装上。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42f358ce3aa8421f9c6bcd7f3aef06cf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后在 <strong>Tools -> Material Themes -> Material Themes Choosers</strong> 选择自己喜欢的主题就可以了。<strong>个人比较推荐 Darker 主题</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b75aff54d7584bdeace32710b1872681~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">界面</h2>
<p>首先先来看看 WebStorm 的界面排布都有啥内容。先看上面这一条：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9770443a93647b280d804008e5a4b35~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>左边这一块这代码导航栏，基本用不太上</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2334383e12904146a053fcd94e0241b6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>右边这一块用的比较多的可能是运行、debug、commit，别的也很少用</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/570530ea898d4c1bbc19328035055489~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>比较牛一个一功能就是 Search Every，快捷键是双击 shift：<strong>shift-shift</strong>，相当于 Mac OS 的 Spot Light 功能。只要被定义好的东西，无论文件、函数、变量、操作都能被搜到。</p>
<p><strong>这么多的快捷键，只要记住这个快捷键就可以一把梭了。</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e984e3ac4984946aeb4349b7b78e4ad~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>比如，我想要 commit 代码，但是找不到按钮，就可以搜索 git commit，下面第二个就是 commit 操作了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7be3fca1c01458bbb229c46bec7e154~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>再来看看左边的界面，是我们很熟悉的文件树。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f592376753a465fa981195a21f79832~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>不知道为什么 Jetbrains 不能自动定位到当前打开这个文件，比如你打开是 A 文件，但是文件树显示的是 B 文件高亮，你要点一下这个圆坨坨才可以定位到当前文件。</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/052e98fcca404f1ca0c1c14493d0b99d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中 Pull Requests 可以连接到 Github 上的 PR 功能，但是如果你在写公司项目和个人项目，那这个功能对你来说没什么用。Structure 和 Favorites 也用的很少，不多说了。</p>
<p>下面的界面功能更多了，而用的比较多是 Git 的操作，别的看一眼就知道怎么回事了。像 TODO 就是检测项目里的 <code>//TODO</code>，Problems 会检测项目里的 TSLint 或 ESLint 错误，Terminal 就是终端。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/961f77d854d7402da80aa0e90b4c7c7b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">Git</h2>
<p>Git 的操作在 Jetbrains 里算一个重量级功能，几乎秒杀市面上的 Git 客户端。打开下面的 Git 就可以看到面板了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f3223207de64b6889a9eccc2751593c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>中间是 Git 的历史，右边可以看到对应修改的文件内容。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c1867631d2c42718d69bdfc9f4a99b9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于分支的管理，可以点右下角的 main（当前我的分支）：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/794a87f6897042bfb072def7a3b75712~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>每个分支都有对应的 push, update(pull), diff, rename, 和 checkout 操作。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/382b14a6436c459f8cfe68d62f92a992~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当需要 commit 的时候，可以使用 <strong>command + k</strong> 来提交：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a9179a67e194164aabd022992c53d7d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>只需要关注绿色的 diff 变化，红色的 commit message 还有右边的提交之前一些操作就可以了。一般来说，用的最多的是 <strong>Amend commit</strong>, <strong>Analyze Code</strong>, <strong>Check TODO</strong> 和 <strong>Optimize imports</strong>。</p>
<p>而 push 则可以使用 <strong>command + shift + k</strong> 来推代码。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79b65192254e44f499825680179d8d9e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然，Jetbrains 不会让你马上就推到远端的。可以选择要推到哪个远程分支，默认就是同名的远程，当然也可以重命名，或者推到另一个远程分支。当然这个功能应该很少人用到。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a65eca7a617747ebaf719a4cb51b0fc6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 push 前你还要以选择推到哪个仓库，默认就是 origin 嘛。如果你有两个仓库要维护，也可以点一下 origin，点击 <strong>Define remote</strong> 来设置另一个远端仓库。虽然这个功能不经常用，我也就用过一两次，不过这功能真爽啊。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05cdf89c9d2448b9b8e132ff974be29e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">本地 History</h2>
<p>除了 Git 可以查文件的改动，Jetbrains 还有一个 <strong>Local history</strong> 功能来记录你文件的改动。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d028e5db0814da1990a5d077923eb26~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fc22ea0a2284daabf66610451610f6a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然看起来像是 Git History，但是这个其实是 Jetbrains 自己维护的一个本地的缓存记录，和 Git 无关，有的时候可能起到救命作用。</p>
<h2 data-id="heading-6">重构</h2>
<p>重构功能很简单，单独立开个标题来说，是因为 Jetbrains 的文件依赖和索引做得太好了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd789f7d70fb4d4c9e0d42caf5b4195c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>只要用上 <strong>Refactor</strong> 功能，直接芜湖起飞，谁用谁知道。我常用的两个功能就是 Rename 和 Move File。</p>
<p>另一个常用的功能，比如你在 A 文件定义了一个 <code>foo</code> 变量，想将它移到 B 文件，就可以选中那个变量，右键 Refactor，再 Move 到另一个文件就可以了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7157d012e244537826b2aade9e3fe3e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/828b0c0e82044e178e73c87fd070756f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有 <code>import</code> 都会一起更新。</p>
<p>刚开始我也有点不敢用这个功能，因为总是怕会不会某个地方没有给我改好呢？但是用了一段时间后，真香，这么说吧：用 Jetbrains 来重命名比我自己重命名都要放心得多。</p>
<h2 data-id="heading-7">运行 & 调试</h2>
<p>按理来说，前端是不会有运行按钮的，因为一般我们都会在命令行 <code>npm run dev</code>。和 VsCode 一样的，WebStorm 一样在 <code>package.json</code> 里提供了运行按钮：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd83671ae9dc4816b03bb14d7117796b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>只要点一下就能运行，<strong>同时会生成一份运行的配置文件</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31609ccc2e0e47eb8822386fd44879ff~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>选择不同的运行配置文件就可以点击运行按钮来运行了。你可能会说：这有什么鬼用呢？当你在运行测试用例的时候就非常好用了：点击测试用例的运行按钮，就可以得到一份配置文件。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5837eceb8d640698b4bfc165b637688~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在这份配置文件里就可以填入一些参数和设置，如 <code>--watch</code>，或者 <code>env=test</code> 这样的参数。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0463241d66e3421289caab91b4177250~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>WebStorm 同时还有强大的 debug 系统。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5791a490231421788d42017a188911e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>相信这一排按钮大家都很熟悉，分别是 step over, step into, force step into, step out</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c4b0e044aaf4d2dbb42a6ef745c5a9b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而最右侧则是 <strong>Evaluate Expression</strong>，Jetbrains 家族又一个哇塞的功能，可以使得在当前执行一些简单的运算：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3654904e6cb41bdadf3b3f767d368f4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时，还能在断点处设置条件断点，这种断点一般用在 for 循环和 if 语句中比较常见</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/576202f12bf845cdbe54fa0c4a8805e6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 <code>i === 5</code> 时停下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ba1dcab23744b77b7a5cec52480518c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>新出的 WebStorm 版本还能直出测试覆盖率。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/880fb98d7bd34708a64f194896c37111~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在右侧面板可以看到当前整个项目中当前目录的文件测试覆盖率情况，连 <code>istanbul</code> 都默默流泪。</p>
<h2 data-id="heading-8">Docker</h2>
<p>要在 Webstorm 使用 Docker，双击 shift 输入 <strong>services</strong> 就会出现 services 面板，选中 <strong>Docker Connection</strong> 点击 OK 就可以连接到本地的 Docker 了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e44c5e8f190e43c29dd163b96723eafc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>pull image（MySQL 的 iamge 在 M1 电脑有点问题）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8efa7ddc729e418aae8b5e37e641b4f7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建容器。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18d2cef3272f47e1b1af18eb42b5f26e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d327a10127574371b2bd7dc4616e0288~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
镜像和容器一目了然。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9939b57482b429ab72cee1edea54a5f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">数据库</h2>
<p>市面上有很多的数据库客户端，如 Mysql workbench, Navigator 等，Jetbrains 依然有自己提供的数据库客户端插件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a793e64188db451495e7b45644d062e3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>注意：最好装牛逼版（要钱/License），牛逼版是 Database Tools and SQL for Webstorm，乞丐版（免费）可以用 Database Navigator。</strong></p>
<p>装好后，在右侧点开数据库，创建一个连接。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f64c0fbe77b41b5a779de698b8eed92~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>配置一下 Host, 端口，账号和密码。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75a3bfd390284c8eb32b545d36cb9794~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建好后随意添加一个 table。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26211ace86be42f9af29e0882be2f2f9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>操作数据库从未有过如此丝滑。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3363ba8c2e614cacab171ddf538d7965~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>最 Amazing 的是代码可以直接和数据库联动，我 TMD 直接绝了。</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7b0cfb0388c4998b7dd6bf360c7cac2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">更多</h2>
<p>说了这么多，也只是说了 WebStorm 一些简单功能操作，更多好玩的玩法还等着大家去探索。比如，最近发现了这个 Jetbrains 聊天室。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cee27029e564c5d955e2c3b12ca6f8b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e2b7a850e864528abd70c837d0f14c9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我感觉边写代码边摸鱼还能当主播的日子已经快来了。</p>
<h2 data-id="heading-11">VsCode vs WebStorm</h2>
<p>最后来说一说我对 VsCode 和 WebStorm 这两个软件的看法吧，纯主观感受（求生欲极强）。我是在 2018 年放弃的 VsCode，导火索是因为有一次两个插件互相冲突了，看了很多个 Issue，直接弃坑了，当时对 VsCode 非常失望。</p>
<p>曾经的我也希望用一个简单的编辑器配置成 IDE 的模样，给我啥我开发啥，插件一顿装。后来，我累了，觉得这么折腾时间不值得。</p>
<p><strong>而且，我慢慢觉得当你要开始开发一个真正的产品时，开发就是一件很严肃的事件，必须把把刀都是锋利的，不能在我做饭的时候才去磨刀或者对比哪把刀更好，这是我放弃 VsCode 的主要原因之一。</strong></p>
<p>VsCode 另外一些不好的点我也可以说一下，而且这是我觉得 VsCode 很难纠正的一些点，希望大家理性看待：</p>
<p><strong>插件太多了。</strong> 多意味着要对比，所以要花很多时候看 README 来甄别哪个插件提供了哪些功能，这些功能适不适合自己。</p>
<p><strong>插件是免费的。</strong> 免费意味着质量不能保证，看起来像免费的，但是浪费的是你对比插件、翻找功能、解决插件冲突的时间。</p>
<p><strong>太多重复的轮子，很多小团体都想在插件市场分一杯羹。</strong> 所以会有很多很像的插件，比如搜一个 <strong>less</strong>，会出现：Sass/Less/Typescript/Jade/Pug Compile-Superhero，Beautify css/sass/scss/lessmichelemelluso.code-beautifier，Easy Less，Less intellsense。请问我要选哪个一呢？既有大而全，又有小而美。独立来看都很好，但是一装起来就免不了功能冲突，功能冗余的问题。</p>
<p>总的来说，VsCode 插件生态是很繁荣的，但是也是一把双刃剑。如果你是 VsCode 大神，各种插件玩得齐活（就像以前那些 Vim 大神），那我也得喊你一声<strong>大哥</strong>。<strong>如果玩不 6 的，不妨试试 WebStorm。</strong></p></div>  
</div>
            