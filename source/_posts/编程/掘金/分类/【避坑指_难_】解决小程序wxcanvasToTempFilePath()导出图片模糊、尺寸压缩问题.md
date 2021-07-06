
---
title: '【避坑指_难_】解决小程序wx.canvasToTempFilePath()导出图片模糊、尺寸压缩问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04526c7762e34abba500c69dd683d6d7~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 01:59:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04526c7762e34abba500c69dd683d6d7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>wx.canvasToTempFilePath(Object object, Object this)</p>
<p>把当前画布指定区域的内容导出生成指定大小的图片。在 draw() 回调里调用该方法才能保证图片导出成功。</p>
</blockquote>
<p>官方的举例🌰</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">wx.canvasToTempFilePath(&#123;
  <span class="hljs-attr">x</span>: <span class="hljs-number">100</span>,
  <span class="hljs-attr">y</span>: <span class="hljs-number">200</span>,
  <span class="hljs-attr">width</span>: <span class="hljs-number">50</span>,
  <span class="hljs-attr">height</span>: <span class="hljs-number">50</span>,
  <span class="hljs-attr">destWidth</span>: <span class="hljs-number">100</span>,
  <span class="hljs-attr">destHeight</span>: <span class="hljs-number">100</span>,
  <span class="hljs-attr">canvasId</span>: <span class="hljs-string">'myCanvas'</span>,
  <span class="hljs-function"><span class="hljs-title">success</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(res.tempFilePath)
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我的实例🌰</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-function"><span class="hljs-title">getCanvas</span>(<span class="hljs-params">path</span>)</span> &#123;
    <span class="hljs-keyword">var</span> that = <span class="hljs-built_in">this</span>
    wx.getSystemInfo(&#123;
      <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
        <span class="hljs-keyword">var</span> pixelRatio = res.pixelRatio;
        <span class="hljs-keyword">var</span> width = res.windowWidth 
        <span class="hljs-keyword">var</span> height = res.windowHeight
        <span class="hljs-keyword">var</span> gap = <span class="hljs-number">40</span> <span class="hljs-comment">//图片边框</span>
        that.setData(&#123;
          <span class="hljs-attr">width</span>: width,
          <span class="hljs-attr">height</span>: height,
          <span class="hljs-attr">gap</span>: gap,
          <span class="hljs-attr">pixelRatio</span>: pixelRatio,
        &#125;)
        wx.getImageInfo(&#123;
          <span class="hljs-attr">src</span>: that.path,
          <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
            that.canvas = wx.createCanvasContext(<span class="hljs-string">"image-canvas"</span>, that)
            that.canvas.drawImage(that.path, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, that.data.width, that.data.height)

            wx.showLoading(&#123;
              <span class="hljs-attr">title</span>: <span class="hljs-string">'数据处理中'</span>,
              <span class="hljs-attr">mask</span>: <span class="hljs-literal">true</span>
            &#125;)
            that.canvas.setStrokeStyle(<span class="hljs-string">'fff'</span>)
            <span class="hljs-comment">// 这里有一些很神奇的操作,总结就是MD拍出来的照片规格居然不是统一的</span>
            <span class="hljs-comment">//过渡页面中，对裁剪框的设定</span>
            that.canvas.draw()
            <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
              wx.canvasToTempFilePath(&#123; <span class="hljs-comment">//裁剪对参数</span>
                <span class="hljs-attr">canvasId</span>: <span class="hljs-string">"image-canvas"</span>,
                <span class="hljs-attr">x</span>: that.data.gap, <span class="hljs-comment">//画布x轴起点</span>
                <span class="hljs-attr">y</span>: that.data.gap, <span class="hljs-comment">//画布y轴起点</span>
                <span class="hljs-attr">width</span>: that.data.width - <span class="hljs-number">2</span> * that.data.gap, <span class="hljs-comment">//画布宽度</span>
                <span class="hljs-attr">height</span>: <span class="hljs-number">500</span>, <span class="hljs-comment">//画布高度</span>
                <span class="hljs-attr">destWidth</span>: that.data.width , <span class="hljs-comment">//输出图片宽度</span>
                <span class="hljs-attr">destHeight</span>: <span class="hljs-number">500</span>   , <span class="hljs-comment">//输出图片高度</span>
                <span class="hljs-attr">canvasId</span>: <span class="hljs-string">'image-canvas'</span>,
                <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
                  that.filePath = res.tempFilePath
                  <span class="hljs-comment">// 清除画布上在该矩形区域内的内容。</span>
                  that.canvas.clearRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, that.data.width, that.data.height)
                  that.canvas.drawImage(that.filePath, that.data.gap, that.data.gap, that.data.width - that.data.gap * <span class="hljs-number">2</span>, <span class="hljs-number">500</span>)
                  that.canvas.draw()
                  wx.hideLoading()
                  <span class="hljs-comment">// 在此可进行网络请求</span>

                &#125;,
                <span class="hljs-attr">fail</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
                  wx.hideLoading()
                  wx.showToast(&#123;
                    <span class="hljs-attr">title</span>: <span class="hljs-string">'出错啦...'</span>,
                    <span class="hljs-attr">icon</span>: <span class="hljs-string">'loading'</span>
                  &#125;)
                &#125;
              &#125;);
            &#125;, <span class="hljs-number">1000</span>);
          &#125;
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>出现的问题：图片模糊，画质像被压缩了一样</p>
<p>翻翻文档，发现了下面这个细节
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04526c7762e34abba500c69dd683d6d7~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决办法：本质上就是生成一个更大的图片，因为手机的屏幕设备的像素比现在一般都是超过2的。实际上我们只需要在使用<code>wx.canvasToTempFilePath</code>的时候，设置参数<code>destWidth</code>和<code>destHeight</code>(输出的宽度和高度)为width和height的2倍以上即可。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b22e7e27889b4d7a83febb5df76779b0~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
通过wx.getSystemInfo()获取设备像素比为3</p>
<p>所以在图片导出的时候，需要设置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">destWidth：width * pixelRatio <span class="hljs-comment">// width*3</span>
destHeight：height * pixelRatio <span class="hljs-comment">// height*3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改完后，导出的图片就和拍摄时的图片清晰度保持一致啦</p></div>  
</div>
            