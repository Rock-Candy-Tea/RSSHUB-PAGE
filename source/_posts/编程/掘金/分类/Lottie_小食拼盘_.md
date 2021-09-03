
---
title: 'Lottie_小食拼盘_'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95a311dc0b8f4a5aa6570c4d560d4824~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 01:47:14 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95a311dc0b8f4a5aa6570c4d560d4824~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:-apple-system-font,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei UI,Microsoft YaHei,Arial,sans-serif;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:23px;margin-bottom:5px;font-weight:700;padding-left:10px;border-left:5px solid #773098&#125;.markdown-body h2&#123;font-size:19px;font-weight:700;padding-left:10px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:17px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;font-size:14px;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;display:block;max-width:100%;margin:1em 0;border-radius:6px;box-shadow:2px 4px 7px #999;user-select:none&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-family:-apple-system-font,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei UI,Microsoft YaHei,Arial,sans-serif;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-family:-apple-system-font,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei UI,Microsoft YaHei,Arial,sans-serif;font-weight:400;font-size:.9em;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8;scroll-behavior:smooth&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:14px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5;border-collapse:collapse&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;border:1px solid #916dd5&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">Lottie是什么？为什么叫Lottie? 能否在微信小程序中使用Lottie呢？</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95a311dc0b8f4a5aa6570c4d560d4824~tplv-k3u1fbpfcp-watermark.image" alt="OIP-C.jpeg" loading="lazy" referrerpolicy="no-referrer">
反正截止今天之前我对这个Lottie还一无所知，反正也用不到，管他呢。
可惜出来混的总是要还的，遇到需要使用动画的场景，由于动画过于复杂，靠我一己之力怎么可能短时间内实现呢！！！一顿调（bai）研(du)发现了这个奇妙的Lottie。</p>
<h4 data-id="heading-1">Lottie是什么东东？</h4>
<p>Lottie是支持Android，iOS，Web和Windows多个平台的库（微信小程序也在努力支持啦，但是貌似还没正式开放），并利用Bodymovin插件把Adobe After Effects（AE）动画解析成json文件，并可以在移动端或者Web上进行渲染显示动画。</p>
<h4 data-id="heading-2">为什么叫Lottie?</h4>
<p>一顿找，发现是个女生的名字命名的，嘿嘿。Lottie是以一位德国电影导演和剪影动画的先驱者命名的。她最著名的电影是《阿基米德王子历险记 (1926)》，这是现存最古老的长篇动画片，比迪斯尼的长篇电影《白雪公主和七个小矮人(1937)》早了十多年。</p>
<h2 data-id="heading-3">使用Lottie之前需要准备些啥呢？</h2>
<p>首先当然准备好吃的喝的，不能委屈自己</p>
<h3 data-id="heading-4">AE下载安装</h3>
<p>这个得要点功夫，炎炎夏日，点杯奶茶降降暑先（有好喝的奶茶麻烦推荐一下）</p>
<p>mac版本（windows版本的麻烦好心人补充下）</p>
<p>链接:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpan.baidu.com%2Fs%2F1eL0AFHMITQvvlgiDv1gbDA" target="_blank" rel="nofollow noopener noreferrer" title="https://pan.baidu.com/s/1eL0AFHMITQvvlgiDv1gbDA" ref="nofollow noopener noreferrer">pan.baidu.com/s/1eL0AFHMI…</a>  密码:743w</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.xxmac.com%2Ferror.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.xxmac.com/error.html" ref="nofollow noopener noreferrer">安装无法打开了？请进</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.xxmac.com%2Fcatalina.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.xxmac.com/catalina.html" ref="nofollow noopener noreferrer">还是安装失败？请进</a></p>
<p>还还不行？自个想办法安装吧.....</p>
<h3 data-id="heading-5">bodyMovin下载安装</h3>
<p>貌似看到过是现有的bodyMovin后有的Lottie，感兴趣的小伙伴自个去瞅瞅吧</p>
<h6 data-id="heading-6">1、进去给我把这个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fairbnb%2Flottie-web" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/airbnb/lottie-web" ref="nofollow noopener noreferrer">bodyMovin的包</a>下载下来</h6>
<h6 data-id="heading-7">2、下载后需要再下载一下<a href="https://link.juejin.cn/?target=https%3A%2F%2Faescripts.com%2Flearn%2Fzxp-installer%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://aescripts.com/learn/zxp-installer/" ref="nofollow noopener noreferrer">ZXP</a>才能打开刚下载的build/extension/bodymovin.zxp文件哦</h6>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f0295d952064f96b1c747aaabc81ebf~tplv-k3u1fbpfcp-watermark.image" width="70%" loading="lazy" referrerpolicy="no-referrer">
<h6 data-id="heading-8">3、下载好ZXP后打开，把刚才的bodymovin.zxp拖进来就好了，提示完成，bodyMovin插件就算下载好了</h6>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74c9919d96944fc7a79b4af08595110d~tplv-k3u1fbpfcp-watermark.image" width="70%/" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de684522d3d742708b0583f3b0ca778c~tplv-k3u1fbpfcp-watermark.image" width="70%/" loading="lazy" referrerpolicy="no-referrer">
<p>到这里就算安装好了，点了奶茶的同学先别急着喝，还得做下相应的设置哈</p>
<h6 data-id="heading-9">4、打开AE开启新世界大门</h6>
<p>. 打开“首选项”/“脚本和表达式”（不同版本可能会不一样有的在“首选项”/“常规”）
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7491bc59537749fe9d0cb854d4fd9412~tplv-k3u1fbpfcp-watermark.image" width="70%/" loading="lazy" referrerpolicy="no-referrer">
. 勾选“允许脚本写入文件和访问网络”
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4adb6aa524b34f46b8002a1d9fd30e29~tplv-k3u1fbpfcp-watermark.image" width="70%/" loading="lazy" referrerpolicy="no-referrer">
. 打开“窗口”/“扩展”/bodymovin
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82f4424125ed4708b5e1b27984496e8e~tplv-k3u1fbpfcp-watermark.image" width="70%/" loading="lazy" referrerpolicy="no-referrer">
. 我们就直接导入素材合成（这里我导入了一个测试视频），此时发现扩展窗口已经多了一条数据，勾选后点击文件设置存放地址，然后点击“render”就ok啦，指定的位置已经生成好data.json文件喽
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8246d142c3ae4644bb8f1ecab4822f27~tplv-k3u1fbpfcp-watermark.image" width="70%/" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90177634bf97411b9383cd5b0c4d9d08~tplv-k3u1fbpfcp-watermark.image" width="70%/" loading="lazy" referrerpolicy="no-referrer"></p>
<p>终于拿到了data.json,到这里就可以愉快的喝奶茶啦
（ps:要是懒得下载安装，可以找设计小哥哥小姐姐问问能不能生成哦）</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6726b5071f8a4670ba163f3526b98d39~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG719.jpeg" loading="lazy" referrerpolicy="no-referrer">
<code>今日废话：下班捉到两枚星黛露，愉快的一天圆满结束喽</code></p></div>  
</div>
            