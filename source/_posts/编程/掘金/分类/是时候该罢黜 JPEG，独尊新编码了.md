
---
title: '是时候该罢黜 JPEG，独尊新编码了'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f10d8f6e9e154fa69c6666016c8e37f4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 14 Apr 2021 09:39:08 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f10d8f6e9e154fa69c6666016c8e37f4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://cloudinary.com/blog/time_for_next_gen_codecs_to_dethrone_jpeg" target="_blank" rel="nofollow noopener noreferrer">Time for Next-Gen Codecs to Dethrone JPEG</a></li>
<li>原文作者：<a href="https://cloudinary.com/blog/author/jon_sneyers" target="_blank" rel="nofollow noopener noreferrer">Jon Sneyers</a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2021/time-for-next-gen-codecs-to-dethrone-jpeg.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/Hoarfroster" target="_blank" rel="nofollow noopener noreferrer">霜羽 Hoarfroster</a></li>
<li>校对者：<a href="https://github.com/Kimhooo" target="_blank" rel="nofollow noopener noreferrer">Kimhooo</a>、<a href="https://github.com/PingHGao" target="_blank" rel="nofollow noopener noreferrer">PingHGao</a></li>
</ul>
</blockquote>
<p><img alt="是时候用新一代图像编码格式替换 JPEG 编码格式了" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f10d8f6e9e154fa69c6666016c8e37f4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我对图像编码十分狂热。如今，一场“图像编码之战”正在酝酿之中，而我并不是唯一<a href="https://codecs.multimedia.cx/2020/11/an-upcoming-image-format-war/" target="_blank" rel="nofollow noopener noreferrer">对此有想法</a>的人。显然，作为 JPEG 委员会 JPEG XL 特设小组的主席，我坚定地致力于多年的图像编码的工作。但是，在本文中，我将努力做到公平和中立。</p>
<p>目标很明确：罢黜 JPEG 这位在 <code><img></code> 标签诞生的 25 年以来（其实就是在网络上存在图片以来），一直居于统治地位的 <em>明智却年老的照片压缩大师</em>。JPEG 这个极度出色的图像编码现在已经达到了他的极限。为什么？仅仅提到他缺少对 alpha 透明度的支持，就足以让人烦恼许久，更不用说那色彩深度的 8 位的限制（也是他不支持 HDR 的原因），还有那和与现有技术相比相对薄弱的压缩。显然，进行谋权篡位的时候到了！</p>
<p><img alt="一张棋盘" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8444caa733e40498c0a8511c4547386~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>六名对手正在进入战场，请做好准备 —— 全军出击：</p>
<ul>
<li><strong>JPEG 2000</strong> —— JPEG 小组，这是 JPEG 编码继承者中最早初露头角的一位，不过仅被 Safari 5+ 支持</li>
<li><strong>WebP</strong> —— Google，支持在所有现代浏览器中使用</li>
<li><strong>HEIC</strong> —— MPEG 小组，基于 HEVC，支持在 iOS 原生应用程序使用，但是不被任何一个包括 Safari 在内的浏览器支持</li>
<li><strong>AVIF</strong> —— 开源媒体协会，支持在 Chrome 和 Opera 浏览器中使用，可在 Firefox 中通过开启 <code>image.avif.enabled</code> 使用</li>
<li><strong>JPEG XL</strong> —— JPEG 小组，下一代编码但不被任何浏览器支持</li>
<li><strong>WebP2</strong> —— Google，一个针对 WebP 的实验性质的成功尝试，主要目标是达到与 AVIF 相似的压缩率，同时保持更快的编码和解码速度。</li>
</ul>
<p>由于 <a href="https://chromium.googlesource.com/codecs/libwebp2/" target="_blank" rel="nofollow noopener noreferrer">WebP2</a> 仍处于试验阶段，并且将是与 WebP 不兼容的全新格式，因此对他进行评估尚为时过早。其他图像编码则早已完成，不过完成时间有所不同：JPEG 2000 已经有了 20 年的历史，而 JPEG XL 项目才刚成立一个月。</p>
<p>坦率地说，基于 HEVC 的 HEIC 不是免费，或者说，不是开源的。即使得到了 Apple 的支持，HEIC 也不大可能成为替代 JPEG 的通用编码。</p>
<p>因此，本文重点关注将其余的新的编码（JPEG 2000、WebP、AVIF 和 JPEG XL）与掌控旧政权的 JPEG 和 PNG 比较。</p>
<h1 data-id="heading-0">压缩</h1>
<p>显然压缩是图像编码的重要指标，快来看看数据吧：</p>
<p><img alt="压缩比较" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9ba667ec1a741888d6d8c3635332713~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>JPEG 是为了对相片进行有损压缩而创建，而 PNG 则专用于无损压缩，并在非摄影图像上表现最佳。在某种程度上，这两个编码是互补的，适用于我们实际应用中的各种用例和图像类型。</li>
<li>JPEG 2000 不仅优于 JPEG，而且还可以进行无损压缩。但是在非摄影图像上他落后于 PNG。</li>
<li>WebP 是专为替代 JPEG 和 PNG 所设计的，他在压缩结果上确实击败了两者，不过差距较小。对于高保真、有损压缩来说，WebP 有时甚至会比 JPEG 表现差。</li>
<li>相比 JPEG，HEIC 和 AVIF 更能有效地处理相片的有损压缩。虽然有时他们会在无损压缩方面落后于 PNG，但对于有损的非摄影图像来说会产生更好的结果。</li>
<li>JPEG XL 在压缩效果上突飞猛进，远胜过 JPEG 和 PNG。</li>
</ul>
<p>当有损压缩足够好（比如说针对 Web 图像而言）时，AVIF 和 JPEG XL 都有着比包括 WebP 在内的现有 Web 图像编码有着明显更好的结果。通常，AVIF 在<a href="https://cloudinary.com/blog/what_to_focus_on_in_image_compression_fidelity_or_appeal" target="_blank" rel="nofollow noopener noreferrer">低保真高吸引力</a>的压缩方面处于领先地位，而 JPEG XL 在中保真到高保真方面表现出色。目前尚不清楚这是两种图像格式的固有属性，还是开发编码器的一个关注点。不过无论如何，他们俩都远超 JPEG，领先着几英里。</p>
<h2 data-id="heading-1">低保真度下的编码比较</h2>
<ol>
<li>原图 - PNG 1799446 bytes</li>
</ol>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e0c4749f7854179b40e54996560f949~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>JPEG - 68303 bytes</li>
</ol>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5d3d842c90143bf93d47d7a6db721d9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>JPEG 2000 - 67611 bytes</li>
</ol>
<p><img alt class="lazyload" src="https://res.cloudinary.com/cloudinary-marketing/image/upload/v1613766747/Web_Assets/blog/011.jp2" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>WEBP - 67760 bytes</li>
</ol>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7a34c45a8ae4537991b5a46e14446ca~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="5">
<li>HEIC - 69798 bytes</li>
</ol>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a795cced486b4f78ba42bf0cfca45033~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="6">
<li>AVIF - 67629 bytes</li>
</ol>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49f232ac4103413e9320ed7033942bf4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="7">
<li>JXL - 67077 bytes</li>
</ol>
<p><img alt class="lazyload" src="https://res.cloudinary.com/cloudinary-marketing/image/upload/v1613767179/Web_Assets/blog/011jxl.jxl" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">速率</h1>
<p>对一张全屏的 JPEG 或 PNG 进行解码仅需极短的时间 —— 几乎只在眨眼瞬间。较新的编码能够做到更好地压缩，但这也会增加复杂性。例如，限制 JPEG 2000 的主要因素之一，就是其过高的计算复杂性。</p>
<p><img alt="速率比较" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/462f7881da274eebb46e7d21b11c3f8c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如果图像压缩的主要目标是加快传送速度，那请顺带考虑解码速度。因为通常解码速度比编码速度更重要，毕竟在许多用例中，我们只需编码一次即可，而这一过程可以在强大的机器上离线进行。相反，解码则需要在包括低端设备在内的各种设备上进行多次。</p>
<p>由于 CPU 速度在单核性能方面一直处于停滞状态，因此并行化多核处理变得越来越重要。毕竟，硬件的发展趋势是拥有更多的 CPU 内核，而不是更高的时钟速度。由于在多核处理器成为现实之前设计完成，JPEG 和 PNG 等较旧的编码本质上是顺序的，也就是说，多核对单图像解码没有任何好处。在这方面，JPEG 2000、HEIC、AVIF 和 JPEG XL 都更具前瞻性。</p>
<h1 data-id="heading-3">局限性</h1>
<p>JPEG（至少是事实上的 JPEG）和 WebP 的主要缺点是他们只支持最大的 8 位色彩深度。虽然说对于具有标准动态范围（SDR）和有限色域（如 sRGB）的图像，这个深度就足够了。但对于高动态范围（HDR）和广色域图像，那需要更高的深度。</p>
<p>目前，10 位的色彩深度足以满足图像传送的需要，而其他所有图像编码都支持 10 位的深度。不过对于创作工作流（可能仍需要连续的图像转换）则可能需要更高的深度。</p>
<p><img alt="局限性比较" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/237da6c07e824c05817a09354523f9d1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>WebP 和 HEIC 不支持没有色度二次采样的图像则是另一种限制。对于许多照片，色度二次采样已经足够了。在其他情况下，比如说那些具有精细细节或具有彩色外观的纹理或彩色文本图像上，WebP 和 HEIC 图像的表现可能就差强人意了。</p>
<p>当前，最大尺寸限制对 Web 部署几乎没有问题。但是，对于摄影和图像创作，基于视频编码的格式的限制可能会令人望而却步。请注意，即使 HEIC 和 AVIF 允许在 HEIF 容器级别进行切片，即实际图像尺寸实际上是不受限制的，但在切片边界处可能会出现伪像。例如，Apple 的 HEIC 实现使用大小为 512x512 的独立编码的图块，这意味着在例如另存为 HEIC 时，编码解码器会将原本 1586x752 的图像被切成八个较小的图像块，如下所示：</p>
<p><img alt="编码的分块" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1f1abcabc834097b2d235ba030baac0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如果你放大去关注一下那些独立编码的图块之间的边界，那你肯定能够很清晰地看到图块之间的不连续：</p>
<p><img alt="放大" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a62ce6d8768402283f3e13305440baf~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>为避免此类图块边界伪像，在使用 HEIC 和 AVIF 的时候我们应该避免让图像超过最大每块尺寸（即 8K 视频帧的大小）。</p>
<h1 data-id="heading-4">动画</h1>
<p>最初，GIF、JPEG 和 PNG 都只能表示静态图像。但 GIF 于 1989 年首先支持动画 —— 甚至在其他编码还没有出现之前，这可能是他尽管有其局限性和较差的压缩效果，但在今天仍在被广泛地使用的唯一原因。现在所有主流浏览器还支持动画 PNG（APNG）编码，这是一个<a href="https://caniuse.com/apng" target="_blank" rel="nofollow noopener noreferrer">相对较新的状况</a>。</p>
<p>在大多数情况下，最好使用视频编码而不是为静止图像设计的图像编码对动画进行编码。HEIC 和 AVIF 分别基于 HEVC 和 AV1，是真正的视频编码。尽管 JPEG XL 也支持动画，但他仅执行帧内编码，而没有运动矢量和视频编码提供的其他高级帧间编码工具的功能。即使对于仅运行几秒钟的短视频片段，视频编码的压缩效果也要比所谓的动画静止图像编码（如 GIF 和 APNG 甚至 WebP 动画或 JPEG XL）明显更好。</p>
<blockquote>
<p>注；如果浏览器在 <code><img></code> 标签中接受他们可以在 <code><video></code> 标签中播放的所有视频编码那会好极了！不过唯一的区别是在 <code><img></code> 标签中视频是自动播放、静音且循环播放的。借此这些新的精巧的视频编码格式（例如 VP9 和 AV1），就会被自动地应用于我们的动画之中，让我们最终能够摆脱那古老的 GIF 格式了～</p>
</blockquote>
<h1 data-id="heading-5">功能</h1>
<p>让我们谈回静止的图像。除了快速压缩 RGB 图片（没有大小或色彩深度限制）外，图像编码还必须提供其他所需功能。</p>
<p><img alt="功能对比" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f1843cd20ce4e73a4b69511818ff28b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>对于 Web 图像尤其是大的图像来说，慢慢加载的图像，即<a href="https://cloudinary.com/blog/improve_the_web_experience_with_progressive_image_decoding" target="_blank" rel="nofollow noopener noreferrer">渐进式解码</a>可是一项出色的功能。JPEG 编码系列在这方面最为强大。</p>
<p>此外所有新的编码均支持 Alpha 透明度。最新的还支持深度图，比如说我们可以使用深度图将效果应用于前景和背景。</p>
<p>具有多层的图像（称为叠加层）可以增强 Web 交付。一个典型的例子是我们可以为照片添加清晰的文字叠加层，从而具有更强的压缩效果和更少的伪影。不过，他在创作工作流程中最有用。此外，对于这些工作流程，JPEG XL 还提供了诸如图层名称、选择蒙版、专色通道以及对 16 位整数和 16 位、24 位或 32 位浮点图像进行快速无损编码的功能。</p>
<p>在抵御世代丢失的弹性方面，视频编码不能完全发挥出色的性能。不过对于 Web 交付，这种缺陷并不重要，我指的是在图像变成例如模因，而最终被重新编码多次的情况下除外。</p>
<p><img alt="2000 代" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87ec2d91481d4ef8a5c50db4612fe557~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>最后，JPEG XL 的独特过渡功能是他可以有效地重新压缩<a href="https://cloudinary.com/blog/legacy_and_transition_creating_a_new_universal_image_codec" target="_blank" rel="nofollow noopener noreferrer">旧版 JPEG 文件</a>，而不会产生内容的丢失。</p>
<h1 data-id="heading-6">希望与策略</h1>
<p>最新一代的图像编码尤其是 AVIF 和 JPEG XL，是对旧 JPEG 和 PNG 编码的重大改进。可以肯定的是，JPEG 2000 和 WebP 还可以更有效地压缩并提供更多功能，不过总体效果并不显着且不够稳定，不足以保证快速广泛地采用。AVIF 和 JPEG XL 会做得更好 —— 至少我是这么希望的。</p>
<p>在未来的几十年中，会不会有一个赢家成为主导的编码？如果会有，那会是 AVIF、JPEG XL 还是即将推出的 WebP2？还是 WebP，毕竟他有着广泛的浏览器支持？会不会有多个获胜者，例如 AVIF 是低保真高吸引力的首选编码，而 JPEG XL 是高保真的首选编码？那些新的编码会不会输掉这场战斗，而旧的 JPEG 又能再次在被罢黜的尝试中存活吗？我想回答这些问题为时尚早。</p>
<p>就目前而言，一个好的事件策略可能是同时使用几种不同的图像编码方法。不仅要利用他们的独特优势，还要降低任何一种方法成为<a href="https://www.sisvel.com/licensing-programs/audio-and-video-coding-decoding/video-coding-platform/license-terms/av1-license-terms" target="_blank" rel="nofollow noopener noreferrer">专利巨魔</a>攻击目标的可能性。磁盘空间在这里是无关紧要的，因为相对于存储它们的巨大存储空间，图像编码占用的空间微不足道。</p>
<p>此外，考虑到许多因素在起作用，但并非所有因素都是技术性的，因此很难预测编码采用的成功。我们只是希望新的编码能在这场战斗中取胜，这主要是与惯性和现状的“轻松”相对立的。最终，除非 JPEG 占主导地位，否则无论采用哪种新编码，我们都将受益于更强的压缩、更高的图像保真度和色彩准确性，从而能够使用更具吸引力且加载速度更快的图像。那将是每个人的胜利！</p>
<p><img alt="编码对比" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38dea20f57044248bf4a7f3f2e98a8d9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<h3 data-id="heading-7">注：</h3>
<p>同时，需要注意的是，上面列出的 AVIF 限制适用于当前定义的最高 AVIF 配置文件（“高级”配置文件），实际上有三个规则，像素数不得大于 35651584，宽度不得大于 16384 且高度不得大于 8704。也可以使用不带配置文件的 AVIF，然后适用 AV1 限制：色彩深度最高为 12 位，最大尺寸最高为 65535x65535（如果你选择使用网格，那还能够更大）。对于 HEIC 来说，可以将容器与具有高达 16 位色彩深度和 4:4:4 的压缩率的 HEVC 有效载荷一起使用，尽管大多数硬件实现均不支持该容器。</p>
</blockquote>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            