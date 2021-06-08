
---
title: 'Egret引擎内存优化最佳实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9964'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 20:29:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=9964'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Egret引擎内存优化最佳实践</h2>
<blockquote>
<p>最近我们在开发一款服饰类的中度游戏项目，里面用到了大量的服饰图片。游戏测试过程中发现内存一直在不断增长，在部分低端机型下出现闪退现象，下面来说说解决过程。</p>
</blockquote>
<p><strong>毫无疑问，这是一个对内存进行有效管理的问题</strong>。明确了方向，那我们就从下几步进行排查：
1、排查是否存在内存泄露，看js对象的创建后是否有删除引用，是否有移除侦听；
2、使用对象池，减少重复对象的频繁创建
3、优化图片素材尺寸，减少不必要图片的加载
这样改完之后，测试发现效果并不明显，内存依旧会不断增加。</p>
<ul>
<li><em>难道是图片内存没有释放？</em></li>
</ul>
<p>看着这么大的内存，基本可以明确是图片的原因</p>
<ul>
<li><em>那图片内存要怎样才能释放？</em></li>
</ul>
<p>检查代码已经没有地方对图片进行引用了，按理说应该会被垃圾回收器回收啊！</p>
<ul>
<li><em>怎么办？</em></li>
</ul>
<p>查引擎文档，发现有个RES.destroyRes的API，作用是：销毁单个资源文件或一组资源的缓存数据。
再阅读源码，发现Egret引擎会对资源进行引用，如果不调用RES.destroyRes进行资源释放，图片内存不会进行回收！
<strong>结论：通过引擎加载的所有图片，如果不手动销毁对象，那么图片会一直缓存在内存里面。加载的图片越多，内存占用越大，直到闪退。Egret引擎本身没有任何内存管理策略。</strong></p>
<ul>
<li><em>再接下来怎么办？</em></li>
</ul>
<p>知道了原因，就好办了，针对每个功能模块，在合适的位置，释放图片资源。
游戏素材一般包括以下这些：
1、UI图片，比如弹窗、界面、按钮，一般打包进代码包
2、远程加载的图片，比如大背景，根据用户数据特定加载显示的图片
3、Mp3声音文件</p>
<p><strong>我们制定了以下资源内存管理的策略：</strong></p>
<ol>
<li>针对大的UI素材 png、jpg等，针对每个功能模块，在界面关闭的时候 调用 destroyImage释放图片资源。</li>
<li>针对 远程http的的图片，</li>
</ol>
<p>A、非列表item使用的图片用 reSetImage方法代替设置img.source, 同时关闭界面时 调用destroyImage释放图片资源。
B、滚动列表里面用到的图片 用HttpImageCacheManage 管理，在关闭界面时释放图片资源。
3. mp3声音文件，针对每个功能模块，在关闭界面时释放</p>
<p>下面为几个核心方法的代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
  * 释放资源，一般是释放 eui.image的资源
  * 使用场景: 在界面关闭的时候调用;
  * 使用示例：destroyImage(this.bg);
  * 使用建议：尺寸大于1024的图片对象调用本方法释放掉
  * 参数：支持 资源名，url，或image对象
  */</span> 
 public <span class="hljs-function"><span class="hljs-title">destroyImage</span>(<span class="hljs-params">name:string | eui.Image</span>)</span>&#123;
     <span class="hljs-keyword">if</span>(name <span class="hljs-keyword">instanceof</span> eui.Image)&#123;
         <span class="hljs-keyword">if</span>(name.source)&#123;
             <span class="hljs-keyword">let</span> source = name.source;
             <span class="hljs-keyword">if</span>(DEBUG) <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">"释放："</span> + source)
             name.source = <span class="hljs-string">""</span>;
             <span class="hljs-keyword">if</span>(RES.getRes(<any>source))
                 <span class="hljs-keyword">return</span> RES.destroyRes(<any>source);
         &#125;
         <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
     &#125;
     <span class="hljs-keyword">if</span>(DEBUG) <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">"释放："</span> + name)
     <span class="hljs-keyword">if</span>(RES.getRes(<any>name))
         <span class="hljs-keyword">return</span> RES.destroyRes(<any>name);
     <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
 &#125;
 <span class="hljs-comment">/*
  * 释放Image资源，并设置image新的source 
  * 使用场景: 用本方法 替代 img.source = xxxx; 
  * 使用示例：reSetImage(this.bg, xxxx);
  * 使用建议：尺寸大于512的，或使用过1次后不再使用的图片对象调用本方法释放掉
  */</span>
 public <span class="hljs-function"><span class="hljs-title">reSetImage</span>(<span class="hljs-params">name:eui.Image, newSource:string, nowDestroy:boolean=<span class="hljs-literal">false</span></span>)</span>&#123;
     <span class="hljs-keyword">if</span>(!name) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
     <span class="hljs-keyword">if</span>(name.source)&#123;
         <span class="hljs-keyword">let</span> source = <string>name.source;
         <span class="hljs-keyword">if</span>(source != newSource)&#123;
             <span class="hljs-keyword">if</span>(DEBUG) <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">"释放："</span> + source)
             <span class="hljs-keyword">if</span>(nowDestroy)&#123;
                 <span class="hljs-keyword">if</span>(RES.getRes(source))
                     RES.destroyRes(source);
             &#125;
             <span class="hljs-keyword">else</span>&#123;
                 name.once(egret.Event.COMPLETE, <span class="hljs-function">()=></span>&#123;
                     <span class="hljs-keyword">if</span>(RES.getRes(source))
                         RES.destroyRes(source);
                 &#125;, <span class="hljs-built_in">this</span>)
                 name.source = newSource;
             &#125;
         &#125;
         <span class="hljs-keyword">return</span>;
     &#125;
     name.source = newSource;
 &#125;
     
enum HttpImageTYPE &#123; type1, type2, type3&#125;; <span class="hljs-comment">//图片类型分类</span>
<span class="hljs-comment">/**
 * 图片缓存管理：针对部分不适合在更换source时释放的Http图片，采用标记的形式管理，在界面关闭的时候释放
 * 使用方法：
 * item里面：  HttpImageCacheManage.add(HttpImageTYPE.type1, url);
 * ui.hide里面： HttpImageCacheManage.destroy(HttpImageTYPE.type1);
 *  */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HttpImageCacheManage</span> </span>&#123;

    private <span class="hljs-keyword">static</span> pools = &#123;&#125;;

public <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
&#125;

    <span class="hljs-comment">//把素材按类型添加到列表中，方便后面释放</span>
    public <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">type:number, url:string</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(!<span class="hljs-built_in">this</span>.pools[type]) <span class="hljs-built_in">this</span>.pools[type] = &#123;&#125;;

        <span class="hljs-keyword">if</span>(!<span class="hljs-built_in">this</span>.pools[type][url])
            <span class="hljs-built_in">this</span>.pools[type][url] = <span class="hljs-number">1</span>;
    &#125;

    <span class="hljs-comment">//根据type类型释放对应的素材</span>
    public <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">destroy</span>(<span class="hljs-params">type:number</span>)</span>&#123;
        <span class="hljs-keyword">let</span> list = <span class="hljs-built_in">this</span>.pools[type];
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> list)&#123;
            <span class="hljs-keyword">let</span> texture = RES.getRes(key);
            <span class="hljs-keyword">if</span>(texture && texture.$bitmapData)&#123;
                <span class="hljs-keyword">let</span> hashCode = texture.$bitmapData.hashCode;
                <span class="hljs-keyword">var</span> tempList = egret.BitmapData[<span class="hljs-string">"_displayList"</span>][hashCode];
                <span class="hljs-keyword">if</span>(tempList && tempList.length > <span class="hljs-number">0</span>) <span class="hljs-keyword">continue</span>; <span class="hljs-comment">//表示正在使用</span>
            &#125;
            <span class="hljs-keyword">if</span>(DEBUG) <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">"释放："</span> + key)
            RES.destroyRes(key);
            <span class="hljs-keyword">delete</span> list[key]
        &#125;
        <span class="hljs-keyword">if</span>(DEBUG)&#123;
            <span class="hljs-keyword">if</span>(HttpImageCacheManage[<span class="hljs-string">"dtime"</span>]) egret.clearTimeout(HttpImageCacheManage[<span class="hljs-string">"dtime"</span>]);
            HttpImageCacheManage[<span class="hljs-string">"dtime"</span>] = egret.setTimeout(<span class="hljs-function">()=></span>&#123;
                <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">"释放资源后内存占用："</span>);
                RES.profile();
            &#125;, <span class="hljs-built_in">this</span>, <span class="hljs-number">20</span>);
        &#125;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>请特别注意的是：</strong>
在释放图片资源时需要判断图片是否正在使用，比如A界面用到了图片1，B界面也用到了图片1，B界面关闭的时候就不能把图片1释放掉，图片资源（egret.Texture）在内存里面是共用的，如果释放了，在A界面图片就显示不出来了。</p>
<p>Egret引擎没有提供egret.Texture 是否正在使用的方法，需要我们自己读取私有变量来判断。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">public <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">checkIsUsing</span>(<span class="hljs-params">resName:string</span>)</span>&#123;
<span class="hljs-keyword">let</span> texture = RES.getRes(resName);
    <span class="hljs-keyword">if</span>(texture && texture.$bitmapData)&#123;
         <span class="hljs-keyword">let</span> hashCode = texture.$bitmapData.hashCode;
         <span class="hljs-keyword">var</span> tempList = egret.BitmapData[<span class="hljs-string">"_displayList"</span>][hashCode];
         <span class="hljs-keyword">if</span>(tempList && tempList.length > <span class="hljs-number">0</span>)
<span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>; <span class="hljs-comment">//表示正在使用</span>
     &#125;
<span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过以上策略的使用，图片内存得到了有效管理，再重度的游戏，都可以在低端机上正常运行。而且，代码修改成本很低！</p>
<p><strong>最后</strong>，以上方法是基于 Egret引擎RES组件管理素材。有些开发者没有使用RES来管理素材，而是直接使用 egret. URLLoader 或 egret. ImageLoader 来加载的图片素材，这种情况需要怎样释放图片内存呢？
<strong>答：只需要针对不用的图片资源（egret.Texture）调用dispose方法、并删除引用就ok了！</strong></p>
<p><em>本文未经允许，禁止转载~~</em></p></div>  
</div>
            