
---
title: 'Vue 实现简单直播功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b3474dc1ecd45b6aa08adeb045ab461~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 19:12:16 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b3474dc1ecd45b6aa08adeb045ab461~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">Vue 简单实现直播功能</h3>
<h4 data-id="heading-1">1.拥有一个绑定ip的域名</h4>
<h4 data-id="heading-2">2.添加一个推流域名，播流域名</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b3474dc1ecd45b6aa08adeb045ab461~tplv-k3u1fbpfcp-watermark.image" alt="image-20210706104856479.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>按阿里云文档提示配置就可以</p>
<h4 data-id="heading-3">3.播流域名设置跨域</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b879cdf6d0384fb9bc97b93d9e37f779~tplv-k3u1fbpfcp-watermark.image" alt="image-20210706104930137.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">4.把https转http</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32b0c01af2fd4b839be362a4c587a81d~tplv-k3u1fbpfcp-watermark.image" alt="image-20210706105009782.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要下载ssl证书 我用的是 宝塔</p>
<h4 data-id="heading-5">5.地址生成器</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3073700811d745e8ba3432e2636ce19c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210706105212824.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如何关联</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/191fd46096644fc8899194882c372bbc~tplv-k3u1fbpfcp-watermark.image" alt="image-20210706105430408.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击生成后形成</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/312ff51991994b239ba71b1050c221b9~tplv-k3u1fbpfcp-watermark.image" alt="image-20210706105525269.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>推流地址</code></p>
<p>给主播用的 打开 OBS</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/564d7222ffc64b829cde84bf708d5ae5~tplv-k3u1fbpfcp-watermark.image" alt="image-20210706105759720.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15b8e6e85c6e4fbd916a25c1ae753379~tplv-k3u1fbpfcp-watermark.image" alt="image-20210706110154661.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">5.H5我们使用的播放器  DPlayer</h4>
<blockquote>
<p><strong><a href="http://dplayer.js.org/zh/guide.html#special-thanks" target="_blank" rel="nofollow noopener noreferrer">dplayer.js.org/zh/guide.ht…</a></strong></p>
</blockquote>
<p><strong>踩坑</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4061b5b15704577ad814742e72c5c9d~tplv-k3u1fbpfcp-watermark.image" alt="image-20210706110308076.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不同类型的原画播放地址 要下不同的插件</p>
<p>例如 M3U7    下载   hls.js</p>
<pre><code class="copyable"><!-- 现场课堂 -->
<template>
    <div class="app">
        <div id="dplayer"></div>
    </div>
</template>
<script>
/*
  我这里使用的是m3u8流，你们也可以选择其他方式，dplayer官网都有详细介绍。
*/
import DPlayer from "dplayer";
import flv from "flv";
let Hls = require("hls.js");
export default &#123;
    name: "Live",
    methods: &#123;
        live() &#123;
            const dp = new DPlayer(&#123;
                live: true,
                container: document.getElementById("dplayer"),
                video: &#123;
                    url: "http://bbb.yzlhaha.top/aaa/bbb.m3u8?auth_key=1625538630-0-0-42eff5811545acdbb15c42cb47bd9185", // 示例地址
                    type: "customHls",
                    customType: &#123;
                        customHls: function (video, player) &#123;
                            const hls = new Hls();
                            hls.loadSource(video.src);
                            hls.attachMedia(video);
                        &#125;,
                    &#125;,
                &#125;,
            &#125;);
        &#125;,
    &#125;,
    mounted() &#123;
        // console.log(flv);
        this.live();
    &#125;,
&#125;;
</script>
<style scoped>
#dplayer &#123;
    width: 100%;
    height: 500px;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            