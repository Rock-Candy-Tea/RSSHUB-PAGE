
---
title: '微信开放数据域UI绘制解决方案的应用（支持滚动）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1418647f04043928701a50ec881e782~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 05:09:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1418647f04043928701a50ec881e782~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Egret白鹭项目开放数据域接入微信轻量级的Canvas渲染引擎介绍：</p>
<p>微信官方团队发布了开放数据域UI绘制解决方案，<a href="https://developers.weixin.qq.com/community/minigame/doc/0006865cfdc68070919970f4d51801?blockType=2" target="_blank" rel="nofollow noopener noreferrer">详情请戳这里</a>：</p>
<p>使用白鹭项目接入过程中可能会遇到2个坑（使用官方提供的测试用例），下面提供解决办法：</p>
<p><strong>1、界面缩放显示异常</strong>
先放正常效果图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1418647f04043928701a50ec881e782~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
异常效果图如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f19bde452474be0a33513de8b0a878b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
原因是 sharedCanvas 里面绘制的是内容为960px，和白鹭画布有个转换关系，需要对bitmap进行缩放。
在platform.js 加上这一句解决问题：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">bitmap.scaleX = bitmap.scaleY = sharedCanvas.width/<span class="hljs-number">960</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2、在部分机型下界面被裁剪（比如iphone5、iphon6 等低分辨率机型）</strong>
异常效果图如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07e882a2efb94601a1e4576f56b36efc~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
原因是 sharedCanvas 里面绘制的是内容为960px，而手机真实分辨率低于960，不够面积用于绘制，故要对sharedCanvas尺寸进行修改，设置成960宽。
在platform.js 加上下面代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span>(sharedCanvas.width < <span class="hljs-number">960</span>)&#123;
<span class="hljs-keyword">let</span> data = wx.getSystemInfoSync();
sharedCanvas.width = <span class="hljs-number">960</span>;
sharedCanvas.height = <span class="hljs-number">960</span> * data.windowHeight/data.windowWidth;
sharedCanvas.style.width = sharedCanvas.width + <span class="hljs-string">'px'</span>;
sharedCanvas.style.height = sharedCanvas.height + <span class="hljs-string">'px'</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在openDataContext/index.js 加上下面代码进行事件侦听，在打开排行榜时需要强制绘制</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">wx.onMessage(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
init();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改完之后，就能看到正常效果了。</p>
<p>最后，附上 platform.js 里面 WxgameOpenDataContext class的完整代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">WxgameOpenDataContext</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-title">createDisplayObject</span>(<span class="hljs-params">type, width, height</span>)</span> &#123;

<span class="hljs-keyword">if</span>(sharedCanvas.width < <span class="hljs-number">960</span>)&#123;
<span class="hljs-keyword">let</span> data = wx.getSystemInfoSync();
sharedCanvas.width = <span class="hljs-number">960</span>;
sharedCanvas.height = <span class="hljs-number">960</span> * data.windowHeight/data.windowWidth;
sharedCanvas.style.width = sharedCanvas.width + <span class="hljs-string">'px'</span>;
sharedCanvas.style.height = sharedCanvas.height + <span class="hljs-string">'px'</span>;
&#125;

        <span class="hljs-keyword">const</span> bitmapdata = <span class="hljs-keyword">new</span> egret.BitmapData(sharedCanvas);
        bitmapdata.$deleteSource = <span class="hljs-literal">false</span>;
        <span class="hljs-keyword">const</span> texture = <span class="hljs-keyword">new</span> egret.Texture();
        texture._setBitmapData(bitmapdata);
        <span class="hljs-keyword">const</span> bitmap = <span class="hljs-keyword">new</span> egret.Bitmap(texture);
<span class="hljs-built_in">console</span>.log(width,height);
        bitmap.width = width;
        bitmap.height = height;

bitmap.scaleX = bitmap.scaleY = sharedCanvas.width/<span class="hljs-number">960</span>;

        <span class="hljs-keyword">if</span> (egret.Capabilities.renderMode == <span class="hljs-string">"webgl"</span>) &#123;
            <span class="hljs-keyword">const</span> renderContext = egret.wxgame.WebGLRenderContext.getInstance();
            <span class="hljs-keyword">const</span> context = renderContext.context;
            <span class="hljs-comment">////需要用到最新的微信版本</span>
            <span class="hljs-comment">////调用其接口WebGLRenderingContext.wxBindCanvasTexture(number texture, Canvas canvas)</span>
            <span class="hljs-comment">////如果没有该接口，会进行如下处理，保证画面渲染正确，但会占用内存。</span>
            <span class="hljs-keyword">if</span> (!context.wxBindCanvasTexture) &#123;
                egret.startTick(<span class="hljs-function">(<span class="hljs-params">timeStarmp</span>) =></span> &#123;
                    egret.WebGLUtils.deleteWebGLTexture(bitmapdata.webGLTexture);
                    bitmapdata.webGLTexture = <span class="hljs-literal">null</span>;
                    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
                &#125;, <span class="hljs-built_in">this</span>);
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> bitmap;
    &#125;

    <span class="hljs-function"><span class="hljs-title">postMessage</span>(<span class="hljs-params">data</span>)</span> &#123;
        <span class="hljs-keyword">const</span> openDataContext = wx.getOpenDataContext();
        openDataContext.postMessage(data);
    &#125;
&#125;

WxgamePlatform.prototype.name = <span class="hljs-string">'wxgame'</span>;
WxgamePlatform.prototype.openDataContext = <span class="hljs-keyword">new</span> WxgameOpenDataContext();

<span class="hljs-built_in">window</span>.platform = <span class="hljs-keyword">new</span> WxgamePlatform();
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            