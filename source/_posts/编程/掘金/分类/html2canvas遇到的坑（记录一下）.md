
---
title: 'html2canvas遇到的坑（记录一下）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7dfe72fd031e437486063a53e1585a87~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 06:53:15 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7dfe72fd031e437486063a53e1585a87~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>做过html转图片的小伙伴们肯定都用过html2canvas插件，今天就在这边记录下我遇到的坑<br></p>
<p>因为我用的是mui的h5+plus开发，所以在浏览器上功能都是好的，但是一打包成App之后，安卓上一切正常，ios上面就会有各种问题：<br></p>
<p><strong>1、html2canvas SecurityError: The operation is insecure</strong><br></p>
<p>看到这个问题之后都傻眼了，html2canvas的方法都不走了，好，去百度，百度有的说操作不安全，图片跨域等，当时第一想法是图片都是本地的怎么会跨域呢，按照网上说的方法试了都没用，后来发现把<strong>图片地址换成base64</strong>的就可以了，本来以为这个问题解决了就没问题了，开开心心打包测试，然后又遇到问题o(╥﹏╥)o
<br></p>
<p><strong>2、不报错，但是html2canvas的代码不走了</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7dfe72fd031e437486063a53e1585a87~tplv-k3u1fbpfcp-watermark.image" alt="VP&#125;90JFU9S~&#123;(I5D0BTK294.png" loading="lazy" referrerpolicy="no-referrer">
没办法，不报错，也排查不出问题，只能一点点注释代码去审查，最后发现v-for中写了复杂的逻辑也不行0.0，后来改成<strong>在computed计算属性中定义</strong><br>
错误的：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ddf65c987af468eb09a957e11685e3e~tplv-k3u1fbpfcp-watermark.image" alt="a.png" loading="lazy" referrerpolicy="no-referrer">
正确的：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8796cf35a9d94e149567e1c98b8b988c~tplv-k3u1fbpfcp-watermark.image" alt="b.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            