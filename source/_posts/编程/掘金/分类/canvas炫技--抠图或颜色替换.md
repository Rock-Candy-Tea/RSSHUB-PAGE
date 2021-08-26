
---
title: 'canvas炫技--抠图或颜色替换'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1937'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 22:06:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=1937'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://link.juejin.cn/?target=http%3A%2F%2F49.235.109.180%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://49.235.109.180/" ref="nofollow noopener noreferrer">演示地址</a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FaMiing%2Fremove-background" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/aMiing/remove-background" ref="nofollow noopener noreferrer">代码仓库</a></p>
<h3 data-id="heading-0">关键技术</h3>
<p><code>canvas api</code>、 <code>element-ui (el-color-picker、el-upload) </code></p>
<h3 data-id="heading-1">原理解析</h3>
<h4 data-id="heading-2">1. 用户从本地上传一张图片</h4>
<p>我们拿到图片数据并在页面渲染出来，这一步用到了elementui的el-upload</p>
<pre><code class="hljs language-js copyable" lang="js">el-upload.avatar-uploader(
  ref=<span class="hljs-string">"logoUpload"</span>,
  accept=<span class="hljs-string">"image/*"</span>,
  action=<span class="hljs-string">"#"</span>,
  :auto-upload=<span class="hljs-string">"false"</span>,
  :on-change=<span class="hljs-string">"handleStatusChange"</span>
)
  el-button(size=<span class="hljs-string">"small"</span>, type=<span class="hljs-string">"primary"</span>) 点击上传
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里实际上不需要真正上传到服务器，只需要获取到图片的在内存中的url</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">handleStatusChange</span>(<span class="hljs-params">file</span>)</span> &#123;
  <span class="hljs-comment">// console.log(file);</span>
  <span class="hljs-built_in">this</span>.originImg = URL.createObjectURL(file.raw);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拿到url之后可以先把图片用<code>img</code>标签渲染在页面上，这样做的目的是为了获取图片的实际尺寸，方面我们等比例缩放在我们的<code>canvas</code>上。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 图片加载完成</span>
    <span class="hljs-function"><span class="hljs-title">loadImg</span>(<span class="hljs-params">e</span>)</span> &#123;
      <span class="hljs-keyword">const</span> img = e.target;
      <span class="hljs-keyword">const</span> width = img.offsetWidth;
      <span class="hljs-keyword">const</span> height = img.offsetHeight;
      <span class="hljs-built_in">this</span>.imgWidth = width;
      <span class="hljs-built_in">this</span>.imgHeight = height;
      <span class="hljs-built_in">this</span>.canHeight = (height / width) * <span class="hljs-built_in">this</span>.canWidth;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>canvas的width可以根据外层容器来获取</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">const</span> contentWidth = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".origin-box"</span>).offsetWidth;
      <span class="hljs-built_in">this</span>.canWidth = <span class="hljs-built_in">Math</span>.min(contentWidth - <span class="hljs-number">12</span>, <span class="hljs-built_in">this</span>.canWidth);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2. 绘制canvas</h4>
<p>绘制图片到canvas，这一步比较简单，</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//这里需要缩放一下，因为我们的画布已经被缩放了</span>
<span class="hljs-built_in">this</span>.originCtx.scale(<span class="hljs-built_in">this</span>.canWidth / width, <span class="hljs-built_in">this</span>.canWidth / width);
<span class="hljs-built_in">this</span>.originCtx.drawImage(img, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">3. 选中颜色</h4>
<p>点击canvas，我们可以拿到该点上的颜色值，获取方式</p>
<pre><code class="hljs language-js copyable" lang="js">ctx.getImageData(targetX,targetY,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拿到的是imagedate对象，<code>&#123;data, width, height&#125;</code>,data即为我们要的颜色值。</p>
<h4 data-id="heading-5">4. 遍历原图片的颜色值，匹配到选中颜色之后，做对应颜色的替换即可</h4>
<p>核心api： <code>getImageData putImageData</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//获取data</span>
<span class="hljs-keyword">const</span> data = <span class="hljs-built_in">this</span>.imageData.data || [];
<span class="hljs-comment">//遍历并替换</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < data.length; i += <span class="hljs-number">4</span>) &#123;
        <span class="hljs-keyword">const</span> similar = <span class="hljs-built_in">this</span>.isSimilar(_fromColor, data.slice(i, i + <span class="hljs-number">4</span>));
        <span class="hljs-keyword">if</span> (similar) &#123;
          data[i] = _toColor[<span class="hljs-number">0</span>];
          data[i + <span class="hljs-number">1</span>] = _toColor[<span class="hljs-number">1</span>];
          data[i + <span class="hljs-number">2</span>] = _toColor[<span class="hljs-number">2</span>];
          data[i + <span class="hljs-number">3</span>] = _toColor[<span class="hljs-number">3</span>] * <span class="hljs-number">255</span>;
        &#125;
 &#125;
 <span class="hljs-comment">//绘制到目标容器上</span>
 <span class="hljs-built_in">this</span>.transCtx.putImageData(<span class="hljs-built_in">this</span>.imageData, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>isSimilar</code>方法用来判断两个颜色是否相似或相等，这个可以通过参数调整（类似于ps的容差概念），容差值越小，匹配越精准。</p>
<blockquote>
<p>颜色值是rgba格式的，即4个数组为一组，数值都在[0,255]之间，由于el-picker返回的rgba，透明度用的是【0，1】表示的，所以要转换到0-255区间</p>
</blockquote>
<h4 data-id="heading-6">5. undo&redo</h4>
<p>撤销、前进、后退功能还是很有必要的，重复替换操作，可返回历史操作步骤。
创建一个队列（这里用数组代替），每次有新的数据变化添加到队列里，用<code>unshift</code>表示入列<code>pop</code>从队列后面删除。可以设置上限10，队列过大会占用较大内存，不建议设置过大。
维护一个index,理解成指针，表示当前回退的数据在队列中的位置。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">undo</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-built_in">this</span>.index++;
  <span class="hljs-built_in">this</span>.redrawImg();
&#125;,
<span class="hljs-function"><span class="hljs-title">redo</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-built_in">this</span>.index--;
  <span class="hljs-built_in">this</span>.redrawImg();
&#125;,
<span class="hljs-function"><span class="hljs-title">redrawImg</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">const</span> preImageData = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">this</span>.imgStock[<span class="hljs-built_in">this</span>.index]).data;
  <span class="hljs-built_in">this</span>.imageData = <span class="hljs-built_in">this</span>.transCtx.createImageData(
    <span class="hljs-built_in">this</span>.canWidth,
    <span class="hljs-built_in">this</span>.canHeight
  );
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.imageData.data.length; i++) &#123;
    <span class="hljs-built_in">this</span>.imageData.data[i] = preImageData[i];
  &#125;
  <span class="hljs-built_in">this</span>.transCtx.putImageData(<span class="hljs-built_in">this</span>.imageData, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>需要注意的细节：当回退到某一条历史记录，比如index=5,这时候再执行手动操作替换，此时就“穿越”了，需要把index = 5之前的历史都移除。（可能描述有点绕~）</p>
</blockquote>
<p>至此，就完成了核心功能了~</p>
<h3 data-id="heading-7">TODO LIST</h3>
<ol>
<li>增加边缘识别，去除毛边</li>
<li>增加容差选项</li>
<li>尝试视频抠图和替换</li>
<li>。。。</li>
</ol>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2F49.235.109.180%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://49.235.109.180/" ref="nofollow noopener noreferrer">演示地址</a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FaMiing%2Fremove-background" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/aMiing/remove-background" ref="nofollow noopener noreferrer">代码仓库</a></p>
<p>欢迎提意见&star！</p></div>  
</div>
            