
---
title: '关于 Flutter 网络图片加载与缓存使用过程总结 ｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07c46558346e4036939ac776421c9f6c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 01:15:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07c46558346e4036939ac776421c9f6c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p><em>废话开篇：文章内容主要是在使用flutter插件过程中的一些总结。</em></p>
<blockquote>
<p><strong>步骤一、添加第三方插件依赖</strong></p>
</blockquote>
<p>添加插件库：</p>
<pre><code class="hljs language-flutter copyable" lang="flutter">cached_network_image: ^3.0.0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装指令：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07c46558346e4036939ac776421c9f6c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里就遇到了一些问题，工程在引入网络缓存图片组件前已经添加了 dio 网络依赖和 path_provider 本地存储依赖， 但是 cached_network_image 也依赖了上面的两个插件，如果dio 和 path_provider的版本跟 cached_network_image 的版本不匹配会报错，不过没关系，报错时终端会提示应加载的依赖组件的版本号，这里根据提示修改好，再执行安装插件指令即可。</p>
<p>这里将 dio 版本升级到 4.0.0 后发现之前到拦截器对象报错，查看版本后发现不但是拦截器对象的 onRequest、onResponse、onError方法的声明参数变了，返回值也发生了变化，这里记录一下。</p>
<pre><code class="hljs language-flutter copyable" lang="flutter">Interceptor dInter = InterceptorsWrapper(
  onRequest: (RequestOptions options,RequestInterceptorHandler handler)&#123;
    options.queryParameters.addAll(&#123;'token':'H+0At+PcIWLY1kjg4ws9gqzwsese9322B81ARjj2eMk='&#125;);
    //以前版本这里只return options即可，现在需要返回 handler.next(options)
    return handler.next(options);
  &#125;,
  onResponse: (Response response,ResponseInterceptorHandler handler)&#123;
  //同理
    return handler.next(response);
  &#125;,
  onError: (DioError error,ErrorInterceptorHandler handler)&#123;
  //同理
    return handler.next(error);
  &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>步骤二、简单封装一下网络加载图片组件</strong></p>
</blockquote>
<pre><code class="copyable">import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class GeneralFadeInImage extends StatelessWidget &#123;
  String image;
  BoxFit fit;
  String placeholder;
  double width;
  GeneralFadeInImage(&#123;required this.image,this.fit = BoxFit.fill,this.placeholder = 'assets/images/placeholderimg.png',this.width = 0&#125;);
  
  //加载网络图片及缓存
  Widget _cacheImage()&#123;
    return (this.width == 0) ? CachedNetworkImage(
      imageUrl: this.image,
      fit: this.fit,
      placeholder: (context, url) => Image.asset(this.placeholder,fit: this.fit,),
      errorWidget: (context, url, error) =>
          Image.asset('images/image-failed.png'),
    ) : CachedNetworkImage(
      imageUrl: this.image,
      fit: this.fit,
      width: this.width,
      placeholder: (context, url) => Image.asset(this.placeholder,fit: this.fit,),
      errorWidget: (context, url, error) =>
          Image.asset('images/image-failed.png'),
    );
  &#125;

  //加载网络图片
  Widget _loadNetworkImage()&#123;
    return (this.width == 0) ? new FadeInImage.assetNetwork(
        placeholder: this.placeholder,
        image: this.image,
        fit: this.fit,
        imageErrorBuilder: (context, error, stackTrace) &#123;
          return Image.asset(this.placeholder,fit: this.fit,);
        &#125;) : new FadeInImage.assetNetwork(
        placeholder: this.placeholder,
        width: this.width,
        image: this.image,
        fit: this.fit,
        imageErrorBuilder: (context, error, stackTrace) &#123;
          return Image.asset(this.placeholder,fit: this.fit,width: this.width,);
        &#125;);
  &#125;
  @override
  Widget build(BuildContext context) &#123;
    return _cacheImage();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>步骤三、使用操作</strong></p>
</blockquote>
<p>初始化必填项仅为网络图片地址</p>
<pre><code class="hljs language-flutter copyable" lang="flutter">new GeneralFadeInImage(image: url)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后封装一个缓存管理类，实现获取缓存图片大小及清除缓存图片功能，ImageCache还可获取缓存图片的数量、设置缓存的图片最大数量（默认是1000）等api。</p>
<pre><code class="hljs language-flutter copyable" lang="flutter">import 'package:flutter/cupertino.dart';

class WSLCacheImageManager &#123;
  //读取图片缓存大小
  static String getAllSizeOfCacheImages()&#123;
    ImageCache? imageCache = PaintingBinding.instance!.imageCache;
    String cacheSizeStr = '0 kb';
    if(imageCache != null) &#123;
      int byte = imageCache.currentSizeBytes;
      if(byte >= 0 && byte < 1024) &#123;
        cacheSizeStr = '$byte B';
      &#125; if(byte >= 1024 && byte < 1024 * 1024) &#123;
        double size = (byte * 1.0 / 1024);
        String sizeStr = size.toStringAsFixed(2);
        cacheSizeStr = '$sizeStr KB';
      &#125;else &#123;
        double size = (byte * 1.0 / 1024) / 1024;
        String sizeStr = size.toStringAsFixed(2);
        cacheSizeStr = '$sizeStr MB';
      &#125;
    &#125;
    return cacheSizeStr;
  &#125;

  //清除所有图片缓存
  static void clearAllCacheImage()&#123;
    ImageCache? imageCache = PaintingBinding.instance!.imageCache;
    if(imageCache != null) &#123;
      imageCache.clear();
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了，文章没有太多技术含量，纯属个人使用总结，或许有的朋友也会有过类似的思考。写下来，记录一下，代码拙劣，大神勿喷，如果对大家有帮助，更是深感欣慰。</p></div>  
</div>
            