
---
title: '『 禁止吸烟🚭』纯 CSS 实现 _ 禁烟也能做的这么酷炫'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/570857f784f74f56afbd0ef2a20baee2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 22:30:17 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/570857f784f74f56afbd0ef2a20baee2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin:30px 0 10px;color:#cca152;position:relative;padding-left:50px;border-bottom:2px solid rgba(209,163,78,.6);padding-bottom:0&#125;.markdown-body h1&#123;font-size:30px&#125;.markdown-body h1:before&#123;content:"";width:50px;height:42px;display:block;position:absolute;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAAhBAMAAACo1K8bAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAFZaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA1LjQuMCI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIj4KICAgICAgICAgPHRpZmY6T3JpZW50YXRpb24+MTwvdGlmZjpPcmllbnRhdGlvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CkzCJ1kAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAnUExURUdwTMyhUsqkUMyhUsyiUcyhUsyhUsyhUcyhUsyhUs2hUtytWNWoVX44si8AAAAKdFJOUwD8Bfcge95QncCWSSDAAAABh0lEQVQoz2WSPUvDQBjHjyPSOB7drh2OUOs36NA6pKAFwaEo4tDFIUWxGYLgKw4BEYUuHaQg7XJ0kccsUmrT2qUUQZp8KO/y1hSfIYEf/5eHu0MoGU1+sIbSw5Bypd92S+dWWrd34b15vuOPY4QxuvtYZp0lIVk3Zgjt+5zkh12AvBHnbW85BOjXySPwhc5CYcY0OdDh5dEUqIEj4cN8Dty3a1MqYJS4MaWU5wzVLwMMxqGSNQgA/VFa4gf50yhxSUW+db8ACa2gBxfnABVDFYHCPYrc7TLwCepJM8/ZoVsRwpxdHEozHUXd6idwVzFFM5BFmIhQVQjrNdnCvdd48wblI2VHtsAZioSsTYVwLoXvjMXH1icuNgPhQE+Ot1+xi8HeA3d1Df1f1JPVUOmsYLujBjuSySqSXYt+yTwbJ0pcyIhqTrxkn0BazRLizJosxRBued+z0jPD6VewOXl5utHRGmMNK3k0iTkzxpq2/oIQO6gLprF12kT/R20eyzlcg7iwK0dPsz/ibpdsCHweWwAAAABJRU5ErkJggg==) 0 0 no-repeat;background-size:80%;bottom:-10px;left:-2px&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h2:before&#123;content:"";width:50px;height:42px;display:block;position:absolute;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAAhBAMAAACo1K8bAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAFZaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA1LjQuMCI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIj4KICAgICAgICAgPHRpZmY6T3JpZW50YXRpb24+MTwvdGlmZjpPcmllbnRhdGlvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CkzCJ1kAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAnUExURUdwTMyhUsqkUMyhUsyiUcyhUsyhUsyhUcyhUsyhUs2hUtytWNWoVX44si8AAAAKdFJOUwD8Bfcge95QncCWSSDAAAABh0lEQVQoz2WSPUvDQBjHjyPSOB7drh2OUOs36NA6pKAFwaEo4tDFIUWxGYLgKw4BEYUuHaQg7XJ0kccsUmrT2qUUQZp8KO/y1hSfIYEf/5eHu0MoGU1+sIbSw5Bypd92S+dWWrd34b15vuOPY4QxuvtYZp0lIVk3Zgjt+5zkh12AvBHnbW85BOjXySPwhc5CYcY0OdDh5dEUqIEj4cN8Dty3a1MqYJS4MaWU5wzVLwMMxqGSNQgA/VFa4gf50yhxSUW+db8ACa2gBxfnABVDFYHCPYrc7TLwCepJM8/ZoVsRwpxdHEozHUXd6idwVzFFM5BFmIhQVQjrNdnCvdd48wblI2VHtsAZioSsTYVwLoXvjMXH1icuNgPhQE+Ot1+xi8HeA3d1Df1f1JPVUOmsYLujBjuSySqSXYt+yTwbJ0pcyIhqTrxkn0BazRLizJosxRBued+z0jPD6VewOXl5utHRGmMNK3k0iTkzxpq2/oIQO6gLprF12kT/R20eyzlcg7iwK0dPsz/ibpdsCHweWwAAAABJRU5ErkJggg==) 0 0 no-repeat;background-size:70%;bottom:-15px;left:-1px&#125;.markdown-body h3&#123;font-size:18px&#125;.markdown-body h3:before&#123;content:"";width:50px;height:42px;display:block;position:absolute;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAAhBAMAAACo1K8bAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAFZaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA1LjQuMCI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIj4KICAgICAgICAgPHRpZmY6T3JpZW50YXRpb24+MTwvdGlmZjpPcmllbnRhdGlvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CkzCJ1kAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAnUExURUdwTMyhUsqkUMyhUsyiUcyhUsyhUsyhUcyhUsyhUs2hUtytWNWoVX44si8AAAAKdFJOUwD8Bfcge95QncCWSSDAAAABh0lEQVQoz2WSPUvDQBjHjyPSOB7drh2OUOs36NA6pKAFwaEo4tDFIUWxGYLgKw4BEYUuHaQg7XJ0kccsUmrT2qUUQZp8KO/y1hSfIYEf/5eHu0MoGU1+sIbSw5Bypd92S+dWWrd34b15vuOPY4QxuvtYZp0lIVk3Zgjt+5zkh12AvBHnbW85BOjXySPwhc5CYcY0OdDh5dEUqIEj4cN8Dty3a1MqYJS4MaWU5wzVLwMMxqGSNQgA/VFa4gf50yhxSUW+db8ACa2gBxfnABVDFYHCPYrc7TLwCepJM8/ZoVsRwpxdHEozHUXd6idwVzFFM5BFmIhQVQjrNdnCvdd48wblI2VHtsAZioSsTYVwLoXvjMXH1icuNgPhQE+Ot1+xi8HeA3d1Df1f1JPVUOmsYLujBjuSySqSXYt+yTwbJ0pcyIhqTrxkn0BazRLizJosxRBued+z0jPD6VewOXl5utHRGmMNK3k0iTkzxpq2/oIQO6gLprF12kT/R20eyzlcg7iwK0dPsz/ibpdsCHweWwAAAABJRU5ErkJggg==) 0 0 no-repeat;background-size:60%;bottom:-19px;left:-2px&#125;.markdown-body h4&#123;font-size:16px;padding-left:0;border-bottom:1px solid rgba(209,163,78,.6)&#125;.markdown-body h5&#123;font-size:15px;padding-left:0&#125;.markdown-body em&#123;color:#cca152&#125;.markdown-body del&#123;text-decoration-color:#cca152;text-decoration-thickness:2px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:80%;margin:6px auto;box-shadow:0 6px 15px #8e8e8e;display:block;margin:20px auto!important;object-fit:contain;border-radius:8px&#125;.markdown-body hr&#123;border:none;border-top:2px solid #e0c9a1;margin-top:32px 0&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background:#f6efde;color:#b69454;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Mono,Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;background:#fef6e1;border-radius:4px;box-shadow:0 0 8px hsla(0,0%,47%,.45)&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAOCAMAAABaWb9VAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAFZaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA1LjQuMCI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIj4KICAgICAgICAgPHRpZmY6T3JpZW50YXRpb24+MTwvdGlmZjpPcmllbnRhdGlvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CkzCJ1kAAAAJcEhZcwAADsQAAA7EAZUrDhsAAACHUExURUdwTMxCKdc8NvdYT/9hVyLJPABBAGubKNiIOv+/K+ytJBakH9aZG+5QR5VZDOBDPhmtJ8+VGuGjH/CwJR26MR6+NBq0LPW1KBmwKetNRfJUTONHP92fHuSmIeFEPhu3LR29M/BTS+mqIuqsI5qdHyLKPP++Kv9gVf9lW//KLSXXQCTQP//FLMVm5KQAAAAldFJOUwAlPPz7+woBBPu8Mzu+FlRRKmvnweeG+Wqg6mVNXmuc1OCbmjZJWF/9AAABKklEQVQoz3WS6XaCMBCFRzAM++KGsqhtDwES3//5OtmA2uP9A9zwzRoAgBC0QgQrdA68OZsDr229YGHoIEj7Pl0ZOgjKa5lYJ4Rd1vijn3nuD4Qurjmv48o6RFyfbGDnS6DeEXZfk5ZfuBhdPb9I87ECNMh1EFJKIU6agWzaa01NbmLkxznSmmObJBkkUxrERf3i+ftRiZi7ShPCYY64UhTx1AR5CDYoMXkOKEY7GmTcTzeD/FiER68DfSLgSRqEIBoB3P8h3x8RZhBXGJGusJdD6rfCBl0YqvZNkrV9zej2cWlfJWG6fRpyM41qYH+GTPPi2yFLQYC0Qybm5o96lW77kMbcrBKtgeWTsthVamNXFF4I6x0DTPuugsVRFyYpyxzWqNvHJwed8ws7QyP1UwjNjwAAAABJRU5ErkJggg==) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#fef6e1&#125;.markdown-body a&#123;text-decoration:none;color:#d8ac5a;border-bottom:1px solid #d8ac5a&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#93753f;border-color:#93753f&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f4e8c7;border-collapse:collapse&#125;.markdown-body thead&#123;background:rgba(255,227,176,.6588235294);text-align:left;display:table-header-group;border-bottom:1px solid rgba(255,227,176,.6588235294)&#125;.markdown-body tbody&#123;background:rgba(255,247,229,.3882352941)&#125;.markdown-body td,.markdown-body th&#123;padding:7px;line-height:24px;min-width:100px&#125;.markdown-body blockquote&#123;color:#bd954f;padding:1px 23px;margin:22px 0;border-left:4px solid #dcb267;background-color:#fff7e5&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol .task-list-item,.markdown-body ul .task-list-item&#123;list-style:none&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body::marker&#123;color:#dcb267&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .contains-task-list .task-list-item&#123;list-style:none;position:relative&#125;.markdown-body .contains-task-list .task-list-item input[type=checkbox]&#123;position:relative;top:2px&#125;.markdown-body .contains-task-list .task-list-item input[type=checkbox]:before&#123;content:"";display:inline-block;height:12px;width:12px;position:absolute;left:-2px;top:-2px;border:2px solid #cda152;border-radius:5px&#125;.markdown-body .contains-task-list .task-list-item input[type=checkbox]:checked&#123;position:relative;top:2px&#125;.markdown-body .contains-task-list .task-list-item input[type=checkbox]:checked:before&#123;border:none;content:"";display:inline-block;height:17px;width:17px;position:absolute;left:-2px;top:-2px;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAFo9M/3AAAAAXNSR0IArs4c6QAAAYhJREFUOBFjYACC0/MDGsDEiyvr/zOCeUwMJxn/A8HZRUEMYBFGJsZ6kFoQYALiAyAGCgDpA+sFijKeWRj4H1kWpIWBW1SDQcm+BCzOAiK/vr7BcO/gDbAAI4hE1waWgRBnmWCGIwkyKFjnwow0BhsJk9QLncvw5dV1oPE9MCEGmBWrgCKhcFEowyR+PSNYwemFAZ4M/xjMkRWYJm5oAPFB/joDpI1BHHQANgGPDxj+//vfCA4IdJ3GcevgQnAFhlHLwYIgSVA0wABcwY3tFQzokiBFGIEP0wmigW5wZAK5FFkQib0a6NUDcEmgb7AGFpIGZOZqoMFhIAFQknEAJpn9yLLEssFOBCp2IFaDkl0xg6C8FbJyB3gowUS5RdQYBORQYpVB1iwVHIIMwJh///AYTCmYRklNIBFmNi4GeYt0BhnjeIa3dw8wSBlEgDUhxw2yCRgGfHp2geHiqiSwUwUVrFAiFVkjjA1LrjgTHEwhFvosMCZM4NEIUoAtWWNoBGZ70/gN22HiAD2uhAzsYNBZAAAAAElFTkSuQmCC) 0 0 no-repeat;background-size:100%&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><em><strong>我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" target="_blank" title="https://juejin.cn/post/7139728821862793223">码上掘金挑战赛来了！</a></strong></em></p>
<h3 data-id="heading-0">前言</h3>
<p>老婆之前说，如果我抽烟，当初就不会要我，幸好我是一个对烟味极度厌恶的人，虽然曾经年少无知也玩过几根烟，但是对于烟味的排斥致使我最终没有在抽烟的道路上一去不复返，今天就给大家分享一个由纯 <code>CSS</code> 实现的 <code>3D</code> 禁烟效果，希望人人都能拒绝烟草，还我们一个清新的世界。</p>
<p>我们先来看一下最终的效果，具体如下图所示：</p>
<p align="center"><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/570857f784f74f56afbd0ef2a20baee2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="demo1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">基础布局</h3>
<p>首先还是先搭建相关的 <code>html</code> 代码，将基础的架子搭建起来，代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cigarette"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span>></span>Nooooooo<span class="hljs-tag"></<span class="hljs-name">i</span>></span>Smooooooooking<span class="hljs-tag"><<span class="hljs-name">i</span>></span>|<span class="hljs-tag"></<span class="hljs-name">i</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基础的代码很简单，通过 <code>span</code> 标签和 <code>i</code> 标签生成烟头和烟蒂，然后我们需要添加相关的 <code>CSS</code> 样式，让整个效果清晰明了起来，相关的 <code>CSS</code> 如下：</p>
<pre><code class="hljs language-less copyable" lang="less">*&#123;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">font-family</span>: Arial, Helvetica, sans-serif;
&#125;
<span class="hljs-selector-tag">body</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">justify-content</span>: center;
    <span class="hljs-attribute">align-items</span>: center;
    <span class="hljs-attribute">min-height</span>: <span class="hljs-number">100vh</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#222</span>;
&#125;
<span class="hljs-selector-class">.container</span> &#123;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">justify-content</span>: center;
    <span class="hljs-attribute">align-items</span>: center;
    <span class="hljs-selector-class">.cigarette</span> &#123;
        <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
        <span class="hljs-selector-tag">span</span> &#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
            <span class="hljs-attribute">font-size</span>: <span class="hljs-number">1.35em</span>;
            <span class="hljs-attribute">font-weight</span>: <span class="hljs-number">700</span>;
            <span class="hljs-attribute">text-transform</span>: uppercase;
            <span class="hljs-attribute">line-height</span>: .<span class="hljs-number">76em</span>;
            <span class="hljs-attribute">text-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">2px</span> <span class="hljs-number">5px</span> rgba(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, .<span class="hljs-number">25</span>);
            <span class="hljs-attribute">transform</span>: translate(-<span class="hljs-number">50%</span>, -<span class="hljs-number">50%</span>);
            <span class="hljs-attribute">background</span>: rgba(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, .<span class="hljs-number">25</span>);
            <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
            <span class="hljs-selector-tag">i</span> &#123;
                <span class="hljs-attribute">font-style</span>: normal;
                <span class="hljs-attribute">color</span>: <span class="hljs-number">#ec9535</span>;
                <span class="hljs-selector-tag">&</span><span class="hljs-selector-pseudo">:first</span><span class="hljs-selector-tag">-child</span> &#123;
                    <span class="hljs-selector-tag">&</span><span class="hljs-selector-pseudo">::after</span> &#123;
                        <span class="hljs-attribute">content</span>: <span class="hljs-string">'L'</span>;
                        <span class="hljs-attribute">color</span>: <span class="hljs-number">#ccc</span>;
                        <span class="hljs-attribute">text-transform</span>: lowercase;
                    &#125;
                &#125;
                <span class="hljs-selector-tag">&</span><span class="hljs-selector-pseudo">:last-child</span> &#123;
                    <span class="hljs-attribute">color</span>: red;
                    <span class="hljs-attribute">filter</span>: blur(<span class="hljs-number">2px</span>);
                    <span class="hljs-attribute">text-shadow</span>: -<span class="hljs-number">4px</span> <span class="hljs-number">0</span> <span class="hljs-number">2px</span> <span class="hljs-number">#000</span>,
                    <span class="hljs-number">8px</span> <span class="hljs-number">0</span> <span class="hljs-number">20px</span> <span class="hljs-number">#f00</span>,
                    <span class="hljs-number">8px</span> <span class="hljs-number">0</span> <span class="hljs-number">24px</span> <span class="hljs-number">#f00</span>,
                    <span class="hljs-number">8px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">#222</span>,
                    <span class="hljs-number">12px</span> <span class="hljs-number">0</span> <span class="hljs-number">#555</span>,
                    <span class="hljs-number">16px</span> <span class="hljs-number">0</span> <span class="hljs-number">#666</span>,
                    <span class="hljs-number">20px</span> <span class="hljs-number">0</span> <span class="hljs-number">#888</span>,
                    <span class="hljs-number">24px</span> <span class="hljs-number">0</span> <span class="hljs-number">#999</span>;
                &#125;
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过给 <code>span</code> 标签和 <code>i</code> 标签添加相关的样式，最终实现的效果如下图所示：</p>
<p align="center"><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5353d6be49e3475b85230166196686a1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里我们看到了一个平面的禁止吸烟的效果，要实现 3D 的效果，就需要添加更多的 span 标签，因此我们的 html 代码需要进行更新，代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cigarette"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span>></span>Nooooooo<span class="hljs-tag"></<span class="hljs-name">i</span>></span>Smooooooooking<span class="hljs-tag"><<span class="hljs-name">i</span>></span>|<span class="hljs-tag"></<span class="hljs-name">i</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span>></span>Nooooooo<span class="hljs-tag"></<span class="hljs-name">i</span>></span>Smooooooooking<span class="hljs-tag"><<span class="hljs-name">i</span>></span>|<span class="hljs-tag"></<span class="hljs-name">i</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span>></span>Nooooooo<span class="hljs-tag"></<span class="hljs-name">i</span>></span>Smooooooooking<span class="hljs-tag"><<span class="hljs-name">i</span>></span>|<span class="hljs-tag"></<span class="hljs-name">i</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span>></span>Nooooooo<span class="hljs-tag"></<span class="hljs-name">i</span>></span>Smooooooooking<span class="hljs-tag"><<span class="hljs-name">i</span>></span>|<span class="hljs-tag"></<span class="hljs-name">i</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span>></span>Nooooooo<span class="hljs-tag"></<span class="hljs-name">i</span>></span>Smooooooooking<span class="hljs-tag"><<span class="hljs-name">i</span>></span>|<span class="hljs-tag"></<span class="hljs-name">i</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span>></span>Nooooooo<span class="hljs-tag"></<span class="hljs-name">i</span>></span>Smooooooooking<span class="hljs-tag"><<span class="hljs-name">i</span>></span>|<span class="hljs-tag"></<span class="hljs-name">i</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span>></span>Nooooooo<span class="hljs-tag"></<span class="hljs-name">i</span>></span>Smooooooooking<span class="hljs-tag"><<span class="hljs-name">i</span>></span>|<span class="hljs-tag"></<span class="hljs-name">i</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span>></span>Nooooooo<span class="hljs-tag"></<span class="hljs-name">i</span>></span>Smooooooooking<span class="hljs-tag"><<span class="hljs-name">i</span>></span>|<span class="hljs-tag"></<span class="hljs-name">i</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span>></span>Nooooooo<span class="hljs-tag"></<span class="hljs-name">i</span>></span>Smooooooooking<span class="hljs-tag"><<span class="hljs-name">i</span>></span>|<span class="hljs-tag"></<span class="hljs-name">i</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span>></span>Nooooooo<span class="hljs-tag"></<span class="hljs-name">i</span>></span>Smooooooooking<span class="hljs-tag"><<span class="hljs-name">i</span>></span>|<span class="hljs-tag"></<span class="hljs-name">i</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述的基础布局完成后，接下来就需要让这个禁烟效果变成 <code>3D</code> 立体的，并且能够实现自动旋转。</p>
<h3 data-id="heading-2">旋转的 3D NoSmoking</h3>
<p>布局和相关的基础样式已经完成了，但是现在这个效果还是平面的，我们需要将它转变为 <code>3D</code> 效果，那该如何实现呢？其实也不难，还记得<a href="https://juejin.cn/post/7142876546489909285" target="_blank" title="https://juejin.cn/post/7142876546489909285">前面的文章</a>中介绍的 <code>var</code> 属性吗？我们可以在每个 <code>span</code> 的样式中添加相关的数字属性，然后再通过 <code>CSS</code> 的 <code>var</code> 属性来获取相关的数字，并添加对于的旋转角度即可，修改 <code>html</code> 代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"--i:1"</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span>></span>Nooooooo<span class="hljs-tag"></<span class="hljs-name">i</span>></span>Smooooooooking<span class="hljs-tag"><<span class="hljs-name">i</span>></span>|<span class="hljs-tag"></<span class="hljs-name">i</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
...
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"--i:10"</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span>></span>Nooooooo<span class="hljs-tag"></<span class="hljs-name">i</span>></span>Smooooooooking<span class="hljs-tag"><<span class="hljs-name">i</span>></span>|<span class="hljs-tag"></<span class="hljs-name">i</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来只需要再给 <code>span</code> 标签添加一个旋转属性，它就能变成立体 <code>3D</code> 效果，相关 <code>CSS</code> 样式如下：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-tag">span</span> &#123;
    <span class="hljs-comment">//...other code</span>
    <span class="hljs-attribute">transform</span>: translate(-<span class="hljs-number">50%</span>, -<span class="hljs-number">50%</span>) rotateX(calc(var(--i) * <span class="hljs-number">36deg</span>)) translateZ(<span class="hljs-number">25px</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在原有的 <code>transform</code> 属性中，添加一个 <code>rotateX</code> 属性，它的值就根据前面在 <code>span</code> 标签中设置的 <strong><code>--i</code></strong> 来获取，最终实现的立体效果如下图所示：</p>
<p align="center"><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56e876fc771941f6bd611c70d4c6dd3f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1111.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到这里，还需要最后一步，就是让整个效果动起来，只需要使用 <code>CSS3</code> 中的 <code>animation</code> 属性即可，配合 <code>@keyframes</code> 关键词创建相关动画帧，就可以使整个效果动起来了，相关 <code>CSS</code> 代码如下：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-comment">// ...other code</span>
<span class="hljs-selector-class">.cigarette</span> &#123;
    <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
    <span class="hljs-attribute">animation</span>: animate <span class="hljs-number">15s</span> linear infinite;
    
    ... <span class="hljs-selector-tag">other</span> <span class="hljs-selector-tag">code</span>
&#125;

<span class="hljs-keyword">@keyframes</span> animate &#123;
    <span class="hljs-number">0%</span> &#123;
        <span class="hljs-attribute">transform</span>: perspective(<span class="hljs-number">1000px</span>) rotateX(<span class="hljs-number">0deg</span>);
    &#125;
    <span class="hljs-number">100%</span> &#123;
        <span class="hljs-attribute">transform</span>: perspective(<span class="hljs-number">1000px</span>) rotateX(<span class="hljs-number">360deg</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述的动画帧中，我们设置了从 <code>0%</code> 到 <code>100%</code> 的动画效果，将整个视口设置为 <code>1000px</code>，并且旋转水平坐标轴，最终的实现效果可以在这里进行查看<span href="https://code.juejin.cn/pen/7142879683837706274" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7142879683837706274" data-src="https://code.juejin.cn/pen/7142879683837706274" style="display: none" loading="lazy"></iframe></span></p>
<h3 data-id="heading-3">最后</h3>
<p>我们通过 <code>CSS3</code> 的 <code>animation</code> 属性和 <code>transform</code> 属性实现了一个 <code>3D</code> 的禁烟效果，同时，<strong>吸烟有害健康</strong>，为了我们自己的人身健康以及家人的健康，请不要吸烟🚭。</p>
<p><strong>最后，如果这篇文章有帮助到你，❤️关注+点赞❤️鼓励一下作者，谢谢大家</strong></p>
<h3 data-id="heading-4">往期回顾</h3>
<p><a href="https://juejin.cn/post/7143899396646797342" target="_blank" title="https://juejin.cn/post/7143899396646797342">送你一个可爱的大圆脸😁，速来~</a></p>
<p><a href="https://juejin.cn/post/7142876546489909285" target="_blank" title="https://juejin.cn/post/7142876546489909285">这么炫酷的 3D Menu 效果，真的不来看看？</a></p>
<p><a href="https://juejin.cn/post/7141005249711439908" target="_blank" title="https://juejin.cn/post/7141005249711439908">产品经理：你这个效果不行，我想要一个五彩斑斓的黑！我：。。。</a></p></div>  
</div>
            