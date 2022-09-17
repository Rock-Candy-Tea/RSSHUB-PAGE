
---
title: '接入Twitter和Facebook分享踩坑记录'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b4f6c792bb64a56a1f3e878cadaddff~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 19:33:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b4f6c792bb64a56a1f3e878cadaddff~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";@keyframes spin&#123;0%&#123;transform:rotate(0)&#125;to&#123;transform:rotate(1turn)&#125;&#125;.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#36ace1;background-image:linear-gradient(90deg,rgba(217,234,251,.25) 3%,transparent 0),linear-gradient(1turn,rgba(217,234,251,.25) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;color:#36ace1&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"";display:block;position:absolute;left:0;top:0;bottom:0;margin:auto;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAF8UlEQVRIS71Wa2wUVRT+7r0zu9t2t/RBaSioPCpYbIUfaEIQUogSAwZDAlUSGwgg/CBATExMCJH1D2hIfOEjFEUEhViCgBgIUCH44OkjPAMGBVqhpUCfW3Zn5z7MuQOE0hYxMdxJdmd25s53vnO+851leMCLPWA8/CfA2TsvL8n7q+nTFfNLG+4VqInHOeJLDQMzdz/3r4DGGDb9lxu+aPcE7U61JHDMDePcuv0O21ShugOefqDdtBie3Dk6K/O+Ab+qOjJiz7Ahv6c8hbDDwRiQlgYGDOcaWyEcjg8On+j71IpJndjGt9XO+jM7+pkywNvbazIfercieSdoJ4bE5sWjyZqMpDdeaQNXMNC34ME3LV8B56+1w3AOgk+EXe/Ub6uiLB6XdH/G/mYjeBCcFwnt3zQqWt4t4NjjnhzQ1CGkBhwOCMFAB71U0qsYgRlwBtQ1tiEJAy44OBdQUmFK3aWS06NLT+ukZAQoKCCjsfbDmk6p78RwX3ncWffmIj8U4kh6GpEwh+9rGy23LDU4GBrrm9DsuDYIGMAYIC/EUNQ7Cq1hn+WM2TI8f+jEyCmvjfn1FssuojHx6tDkyZOaCzr8TNpASzDAk8amlRIrEylcSGsYrcGIstIYWhgDDIM2BiGH3ywFkGAC1U9n38bpVqWGdk6r4HMWrZZaG1D5KLn0qYyBEAKnG1otAxLR8L7Z9nfP13CJHQ/ST4vK8sVHe8JsU0U6uO5hlexo8PI7vNDQomwoBRAwpSmtgJAAztS3QLsOsmBQlBtFJMQhlbbPUBBUR7o2hqHVddLbRsfCPQJ+u3TPw8uGl1yklAlHIJZKo3//XEhlLCtifPFyM7xwCI/lZ8IKTTBbS7pPLIggZZsSQ+zXbT4UYSsnet3UMM5HPT5LGbrDGYQroClyT2Jwnyj9aN949e8mDCwuRFoqKxRHUJ21BSDRELuQYGhvbMVV32Dp2RuxcfHSRBfAYTsbU9nJdFj5EiLkglHkRInC1xoxKbH9hQJIaTDvxxTCUddWl4wg0dCCtqSPDmoVx4Eitpxh64ZtsT6b5ie6pPRkfF90TllxOzEwmipMKRRgHODGgCuJkqIcvDdC2BZ5Y+tlHHMzkAKghbAxcQqQDiKrFBxhqg5MHTivS1tQ+sdsvaQl5Yd6yfdRXNQLsQwXnq/AQFLXEIIjzBSuNaaR0SuEtkQKl9IKjAsbJaWfzo1USDsM6zceDJfeVGgnhhN2N7YOyo5kJz1pa2AbgfrO1gRwXW6vSRQNtddR+EhvKGmseskgTtY2Q7kucYWWgToPHzyUyXry0iXfnBtfl5f/PaWPvPNW/zkOAQegJHltFE5dSaCskHqPVEnqpMAMEgkPtR1pKxyh/N0/vTToubtH1G3RmLjhM8ubKXfWB2mRa9ySOaWS2uT8lTZ0cI6I52Ngv7zAbW9mQVm1cpytu441P38XeXTlQu+e46nyh+bjLkMZRU0MCYTCJWZSG1y7cBWNURpxBlxqFBfEwGnGGhaYPSNwhpSv4DK+/vPynBk9MqRIiOWs8a2WJTm9a+cgh6SaMIMz9W1WjYHHMtv0wSmZdWB9gdsya/rcYVg7JoffCdqlD6ceTpiY59tM0PhJp5WNvra+BQkejCMyBarr8KKYDcZi8sDaCDKYFIGRk+FnSVXzyTO9JxBwF8DLc1dlLn65ooNEYN0fBsu21fTvL6PXnhxXlnLIqqhYYBian4lQ2Lk9ogiALsimiLC1QYfhlV1Hnxh7JfcMqxrpd7U2GFa5t9nOd7Kr+kg4uWvnCpromlJeXlq3Os3ZLOlrZBmNQf1ybVqpxhbA7mRIOCy1+esDOWhIyDv/+3Q7LRbsqH+rKRJ+nba+/+WW7II1s9vvVBuNr7KNF1WUM1bSt5f1Vq01jUVkKfnx8uoti3Or5rbd9782M61azJz/rFywYU/OyKqK1p5G2MS1Z18tGFDwTkvIxcK9RwaMP3a9/tbc62lPj/Nw5B9ey9Ehy/MY4oEqelgNleuyCgdXJlmc3fO5Ll56r5f+n/f+AWFf9jvBgaHpAAAAAElFTkSuQmCC);animation:spin 2s linear 1s infinite&#125;.markdown-body h1&#123;position:relative;font-size:30px;padding:12px 38px;margin:30px 0&#125;.markdown-body h1:before&#123;width:30px;height:30px;background-size:30px 30px&#125;.markdown-body h2&#123;position:relative;font-size:24px;padding:12px 36px;margin:28px 0&#125;.markdown-body h2:before&#123;width:28px;height:28px;background-size:28px 28px&#125;.markdown-body h3&#123;position:relative;font-size:18px;padding:4px 32px;margin:26px 0&#125;.markdown-body h3:before&#123;width:24px;height:24px;background-size:24px 24px&#125;.markdown-body h4&#123;position:relative;padding:4px 28px;font-size:16px;margin:22px 0&#125;.markdown-body h4:before&#123;width:20px;height:20px;background-size:20px 20px&#125;.markdown-body h5&#123;position:relative;padding:4px 26px;font-size:15px;margin:20px 0&#125;.markdown-body h5:before&#123;width:18px;height:18px;background-size:18px 18px&#125;.markdown-body h6&#123;position:relative;padding:4px 22px;font-size:14px;margin:16px 0&#125;.markdown-body h6:before&#123;width:16px;height:16px;background-size:16px 16px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#36ace1,#dff0fe,#36ace1);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:50px;height:24px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAEgElEQVRIS72Va0xbZRjH/z2FcimbchEQFDYRCIRAAWFQ2MaCXBwmUxYDLGGEcRFkH9wmk04zG0Bo2dwNIisERANqhjqdEmhd4nRbuwpsXDYWLLoRgeG4Chu9QHvMOQ0dpTAKH3y/tDnv8/5/z/Oc//scBv6nxdgoJ14gVYPEuITHdTdHY12gRIH0T0KljlqwthqUFHGtzAEsxqwLtPvkdc+FeeI3BgMeAMEhdOqR1mM7xswBrgmKE8pfIUhtm7fbZsft/i7wc98MtrUFxmbU6ByYgFwxjtFp5Q+WpF1mCy9wajXoqqD4E91saOf603e+5B7t99xTkyZJEiKJAl2DE9Xio1HvrBS8IuhVwVUP503swdJ9QWAw1izaoDs6pQT/655BMS9yy3KYiUoM/7adu7NmtnQfx5zWm8Q8Ui3gyGcddyU8rv/STRNQouDGP5/mhTubX4dpPv3DMzh1qS9LwuPWr+i63WVyn5QYj/4d/i4bqmbpoQ+auvBlQYghX6PE4wTSOzV5EUYlb5Q4MDqLk9/3cMRF27spDSNQamUnWZ4ebNB+OKNCyYVeFCZ5wZ5tiePN/UiP2YoQL0cUX+iFt4sNUiLdcaVvHJLecQiWnKVE8s5LvxAXRWeYgHLre0hecgAN0sxr0XBZgbJUP6OiLnaM4ivZCBrzOWBZEIY9rY5E8pl2nM0KMzzLq5aPiXmRzgbQm2VyR8KGGK/ICAFB6IusbvsDwhRf+n/jtSHc/nsGgjR9V6/1TyLa1wGU+FtnO1CbHQTHTSzIFJOYJ1jwcGLTccMTcyhp7oW4KFJ/SV4/IScrc55kQj07WNuOn94Lpw8kCm/Qv3W5HLjbWxsyfuNUO1TzWjAJBloKt2FBS+Jz6ShiA12NupBdLWugQcmn28lPMkONNql3U5cTSD9Lq+qEUqPFt++G0aKL687wDAqb+pAU7IKCuK2493AOPQ9UCNpib6T1tkg+RZ9KKJcNn8sJc1vac8o16jklLWLuOiDqwvHUIKPw7vtTON+iCDKkl/Cx9FeSYET5um1mHt6jN0Dz9ftwYjORudNjTdaBmi7kxvvA1d6Gjs0X/Q5Sp3tMEMSHre9HnDEZAPFCWUNVdliGJVPvqEP1Hbh4yPj9LadSY6fu6gPsCX+B3mq7NYLv2od8fj4aoViMNQGFijos/XVMTXGavgUisQIle71hwVx9KFEutLVjw8GORTuxoEbeJS7iPrmQyy/sIj2hQpqYHO7ZGs95nnZS4y8K8Pfqrb58UZ+IlKqbqNgfQm8da+pC9xjLqo8foFkau2qaCeXSyvzXfA9SDrp1bxJ/DU/jSJKXEWdBR2J/9U0UpwXTFZ/+8S76h/71FvO4A8sTeuqQThDKalOiPLN3BbhiYlaNsm964elkCztrC4xMqeDqYIus2JdB3cbS5l4MTag44qJt9GxbF4gKThRKY59lW13+KCUQ1pZMEwHKviKx4pFSqXzxCn/X9Gr2NO+zw+cTiTbxmUyCqH3GlsWg2kRNhOnHmhlrFkIvHTZt1borWvMCmRnwH4usn58STiycAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body del&#123;color:#36ace1&#125;.markdown-body code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#282c34;color:#4ec9b0;padding:.24em .46em;margin:0 4px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;font-size:12px;border-radius:10px;padding:15px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#4ec9b0;background:#282c34&#125;.markdown-body a&#123;text-decoration:none;color:#409eff;border-bottom:1px solid #409eff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#007bff;border-bottom:1px solid #007bff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;position:relative;padding:8px 26px;background-color:rgba(54,172,225,.75);margin:16px 0;border-left:4px solid #409eff;border-radius:5px&#125;.markdown-body blockquote:before&#123;content:"❝";top:10px;left:8px;color:#409eff;font-size:20px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:20px;position:absolute;right:8px;bottom:0;color:#409eff;opacity:.7&#125;.markdown-body blockquote>p&#123;color:#fff&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">准备工作</h2>
<p>1、首先需要在HTML的head添加下述meta标签内容，在分享时，Twitter和Facebook会爬取该网站页面的meta内容，然后生成分享卡片。</p>
<p>2、按照下述配置完成后，需要把内容发布上线，否则Twitter和Facebook无法爬取到网页配置的meta信息。</p>
<p>3、完成上面的两个步骤后，使用官方的测试工具测试分享效果，如果配置正确就可以预览到分享的效果：</p>
<ul>
<li>Twitter测试工具：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcards-dev.twitter.com%2Fvalidator" target="_blank" rel="nofollow noopener noreferrer" title="https://cards-dev.twitter.com/validator" ref="nofollow noopener noreferrer">cards-dev.twitter.com/validator</a></li>
<li>facebook测试工具：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.facebook.com/tools/debug/" ref="nofollow noopener noreferrer">developers.facebook.com/tools/debug…</a></li>
</ul>
<p>4、Twitter和Facebook爬取内容填写的url位置有些区别，其中Facebook无法设置自定义内容。</p>
<blockquote>
<p><strong>切记：</strong> 配置完成后，请务必使用上述的测试工具进行测试，否则可能会出现即使配置正确了，在开发测试分享功能的时候，效果也可能没生效。</p>
</blockquote>
<h2 data-id="heading-1">Facebook分享</h2>
<ul>
<li>meta标签内容：</li>
</ul>
<pre><code class="hljs language-ini copyable" lang="ini"><meta <span class="hljs-attr">property</span>=<span class="hljs-string">"og:title"</span> content=<span class="hljs-string">"Remove Image Background for Free"</span>>
<meta <span class="hljs-attr">property</span>=<span class="hljs-string">"og:description"</span> content=<span class="hljs-string">"Remove Image Background for Free"</span>>
<meta <span class="hljs-attr">property</span>=<span class="hljs-string">"og:site_name"</span> content=<span class="hljs-string">"xxxxxx.com"</span>>
<meta <span class="hljs-attr">property</span>=<span class="hljs-string">"og:url"</span> content=<span class="hljs-string">"https://xxxxxx.com"</span>>
<meta <span class="hljs-attr">property</span>=<span class="hljs-string">"og:image"</span> content=<span class="hljs-string">"https://xxxxx.com/image_background.jpg"</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>字段对应关系预览：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b4f6c792bb64a56a1f3e878cadaddff~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>使用<a title ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=">标签即可调用：</a></li><a title ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=">
</a></ul><a title ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=">
<pre><code class="hljs language-ini copyable" lang="ini"><a <span class="hljs-attr">target</span>=<span class="hljs-string">"_blank"</span> href=<span class="hljs-string">"https://www.facebook.com/sharer/sharer.php?u='链接，分享爬取的内容就是这个从这个链接,该链接不会显示在分享卡片上'"</span>>Facebook分享</a>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>为了方便这里封装了方法：</li>
</ul>
<pre><code class="hljs language-ini copyable" lang="ini">/**
 * 快速分享到Facebook
 */
export const <span class="hljs-attr">facebookShare</span> = () => &#123;
  const <span class="hljs-attr">url</span> = encodeURIComponent(<span class="hljs-string">'链接,分享爬取的内容就是这个从这个链接，该链接不会显示在分享卡片上'</span>)<span class="hljs-comment">;</span>
  const <span class="hljs-attr">facebook</span> = `http://www.facebook.com/sharer/sharer.php?u=<span class="hljs-variable">$&#123;url&#125;</span>`<span class="hljs-comment">;</span>
  window.open(facebook, '_blank')<span class="hljs-comment">;</span>
&#125;<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">Twitter分享</h2>
<ul>
<li>meta标签内容：</li>
</ul>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-comment"><!-- 注：下述的twitter:url 链接,即为twitter从这个链接爬取分享的内容  --></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">property</span>=<span class="hljs-string">"twitter:url"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"https://xxxxxx.com"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"twitter:title"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"Remove Image Background for Free"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"twitter:description"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"Remove Image Background for Free"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"twitter:site"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"@PixCut"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">property</span>=<span class="hljs-string">"twitter:image"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"https://xxxxxx.com/image_background.jpg"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"twitter:card"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"summary_large_image"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>字段对应关系预览：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00ab573c6da3440584a599aade995b70~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
</a><ul><a title ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=">
</a><li><a title ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=">使用</a><a title ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=">标签即可调用：</a></li><a title ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=">
</a></ul><a title ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=">
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">target</span>=<span class="hljs-string">"_blank"</span><span class="hljs-attr">href</span>=<span class="hljs-string">"https://twitter.com/intent/tweet?text=自定义内容，可以文字➕链接之类的<span class="hljs-symbol">&amp;</span>via=twitter账号名，会显示@XXX"</span>></span>Twitter分享<span class="hljs-tag"></<span class="hljs-name">a</span>></span>   
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>为了方便这里封装了方法：</li>
</ul>
<pre><code class="hljs language-ini copyable" lang="ini">/**
 * 快速分享到twitter
 */
export const <span class="hljs-attr">twitterShare</span> = () => &#123;
  // 自定义内容
  const <span class="hljs-attr">content</span> = <span class="hljs-string">'点击此处链接领取奖品，可选'</span>
  const <span class="hljs-attr">url</span> = encodeURIComponent(<span class="hljs-string">'链接，可选'</span>)<span class="hljs-comment">;</span>
  const <span class="hljs-attr">text</span> = `<span class="hljs-variable">$&#123;content&#125;</span> <span class="hljs-variable">$&#123;url&#125;</span>&via=<span class="hljs-variable">$&#123;via&#125;</span>`<span class="hljs-comment">;</span>
  // 分享后会显示 “via @张三”
  const <span class="hljs-attr">via</span> = <span class="hljs-string">'张三'</span><span class="hljs-comment">;</span>
  // 拼接链接
  const <span class="hljs-attr">twitter</span> = `https://twitter.com/intent/tweet?text=<span class="hljs-variable">$&#123;text&#125;</span>`<span class="hljs-comment">;</span>
  window.open(twitter, '_blank')<span class="hljs-comment">;</span>
&#125;<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre></a></div>  
</div>
            