
---
title: 'Flutter 做应用开发时 Charles 抓不到接口的解决办法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7da37f560ad84882aadcb27d47db51ef~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 03:07:22 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7da37f560ad84882aadcb27d47db51ef~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">Flutter 使用 Charles进行抓包</h3>
<p>1.问题</p>
<blockquote>
<p>我们在做应用开发的时候，经常需要利用一些工具抓取网络请求接口，这样可以极大的方便接口联调。但是在用 Flutter 做应用开发时 Charles 却抓不到接口，到底是怎么回事呢 ？</p>
</blockquote>
<p>尝试用其它客户端应用请求网络接口，Charles 都是可以成功抓取的，只有 Flutter 应用的接口无法抓到，到底是怎么回事呢 ？</p>
<p>经过一系列调研，发现 Flutter 应用的网络请求是不走手机的系统代理的，也就是说你在系统设置中设置了代理地址和端口号后 Flutter 也不会走你的代理，而抓接口是必须要设置代理的。如果不能走系统代理，那我们只有在代码中动态设置代理来解决问题了。</p>
<p>2.解决办法</p>
<blockquote>
<p>设置http代理：DefaultHttpClientAdapter 提供了一个onHttpClientCreate 回调来设置底层 HttpClient的代理，我们想使用代理，可以参考下面代码</p>
</blockquote>
<blockquote>
<p>dio</p>
</blockquote>
<pre><code class="copyable">
  import 'dart:io'; 
  import 'package:dio/adapter.dart'; 
  import 'package:dio/dio.dart'; 
   floatingActionButton: new FloatingActionButton(
        onPressed: () async &#123;
          
          // 添加这部分代码
          var dio = Dio();

          (dio.httpClientAdapter as DefaultHttpClientAdapter)
              .onHttpClientCreate = (client) &#123;
            client.badCertificateCallback =
                (X509Certificate cert, String host, int port) &#123;
              return Platform.isAndroid;
            &#125;;
            client.findProxy = (url) &#123;
              return 'PROXY 172.25.84.99:8888'; //这里将localhost设置为自己电脑的IP，其他不变，注意上线的时候一定记得把代理去掉
            &#125;;
          &#125;;
      //代码截止

          final response = await dio.get(
              'http://app.gjzwfw.gov.cn/fwmhapp1/code/getverifyCode.do?number=12345678');
          print('$&#123;response.data&#125;');
        &#125;,
        tooltip: 'Increment',
        child: new Icon(Icons.add),
      ),

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>http</p>
</blockquote>
<pre><code class="copyable">  import 'dart:convert';
  import 'dart:io';
  import 'package:dio/dio.dart';
  floatingActionButton: new FloatingActionButton(
        onPressed: () async &#123;
          var httpClient = new HttpClient();
          httpClient.findProxy = (url) &#123;
            return HttpClient.findProxyFromEnvironment(url, environment: &#123;
              "http_proxy": 'http://172.25.84.99:8888',
            &#125;);
          &#125;;

          var uri = new Uri.http(
              't.weather.sojson.com', '/api/weather/city/101210101');
          var request = await httpClient.getUrl(uri);
          var response = await request.close();
          if (response.statusCode == 200) &#123;
            print('请求成功');
            var responseBody = await response.transform(Utf8Decoder()).join();
            print('responseBody = $responseBody');
          &#125; else &#123;
            print('请求失败');
          &#125;
        &#125;,
        tooltip: 'Increment',
        child: new Icon(Icons.add),
      ),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大功告成，然后就可以在flutter应用中对手机进行抓包啦~下面是我成功抓包的记录：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7da37f560ad84882aadcb27d47db51ef~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            