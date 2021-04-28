
---
title: 'Flutter的网络请求'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2c42502a0e84e95a1f96765548256ea~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Apr 2021 01:58:59 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2c42502a0e84e95a1f96765548256ea~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">flutter网络请求库</h2>
<p>在FLutter中，我们通常使用dio来进行网络请求。</p>
<ol>
<li>dio的安装</li>
</ol>
<pre><code class="copyable">dio: ^3.0.10 # 网络请求
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如此安装好后执行pub get 那么我们就可以使用它啦。</p>
<ol start="2">
<li>dio的简单封装</li>
</ol>
<p>我们都知道，要想使用一个框架，仅仅引入进来是不够的还需要我们去进行简单的封装，以便可以在项目中方便的使用</p>
<pre><code class="copyable">import 'dart:convert';
import 'dart:io';

import 'package:dio/dio.dart';
import 'package:dio/adapter.dart';
import 'package:kooielts/base/base_resp.dart';
import 'package:kooielts/base/utils.dart';
import '../config.dart';
import 'encrypt_params.dart';

class HttpManager &#123;
  Dio _dio;
  BaseOptions _options;
  static const int _receiveTimeout = 5000;
  static const int _sendTimeout = 5000;
  static const int _connectTimeout = 5000;

  Future post<T>(String path, Map params) async &#123;
    //params["app_id"] = Config.getInstance().APP_ID;
    print("path:$path");
    print("params$params");
    //params["validation"] = FlutterNoCppSrc.getNetParams(json.encode(params));
    var response = await _dio.post(path, data: params);
    if (response.statusCode == HttpStatus.ok) &#123;
      return response.data["obj"];
    &#125;
    return new Future.error(new DioError(
        request: response.request,
        response: response,
        type: DioErrorType.RESPONSE,
        error: "请求失败"));
  &#125;

  static BaseOptions _getDefOptions() &#123;
    return BaseOptions(
      connectTimeout: _connectTimeout,
      receiveTimeout: _receiveTimeout,
      sendTimeout: _sendTimeout,
      headers: Utils.getHeader(),
      baseUrl: Config.getInstance().API_DOMAIN,
      contentType:
          ContentType.parse("application/x-www-form-urlencoded").toString(),
    );
  &#125;

  // 单例对象
  static HttpManager _instance = HttpManager._internal();

  // 内部构造方法，可避免外部暴露构造函数，进行实例化
  HttpManager._internal() &#123;
    _options = _getDefOptions();
    _dio = Dio(_options);
    // 设置代理 便于本地 charles 抓包
    (_dio.httpClientAdapter as DefaultHttpClientAdapter).onHttpClientCreate =
        (HttpClient client) &#123;
      client.findProxy = (uri) &#123;
        return "PROXY 10.155.43.118:8888";
      &#125;;
      client.badCertificateCallback =
          (X509Certificate cert, String host, int port) &#123;
        return true;
      &#125;;
    &#125;;
  &#125;

  // 工厂构造方法，这里使用命名构造函数方式进行声明
  factory HttpManager.getInstance() => _instance;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>此处我们封装了一个网络请求类，以后我们用此类就可以愉快地进行网络请求了。
注：HttpManager 是单例类。我们在外界只需要调用getInstance就能拿到这个类的对象了。此单例类在_internal私有构造方法中初始化了dio及其他的一些网络配置，我们只需要在外面调用此类的post方法即可进行网络请求。在post(String path, Map params)方法中path是请求的url地址，params是请求参数。同时我们可以在此方法内给params参数增加公共请求。</p>
<ol start="3">
<li>网络模块的基本结构</li>
</ol>
<p>我们在开发一个app时，不只是要把网络请求发送出去，把结果拿回来而已，同时还需要进行其他的一些配置。此时我们需要搭建一个基本的结构。下面图片是我自己写的一个简单结构的结构图</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2c42502a0e84e95a1f96765548256ea~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图中我们可以看出</p>
<ul>
<li>api.dart</li>
</ul>
<p>一个可以简单配置请求地址的dart类，我们可以在此类中配置baseUrl后面的url请求地址。</p>
<pre><code class="copyable">import '../config.dart';

class Api&#123;
  static const String launchInfo = "/api/XXX/web/courses/coursesTypeList";

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>http_manager.dart</li>
</ul>
<p>刚才上面说到的http管理类。</p>
<ul>
<li>config.dart</li>
</ul>
<p>一个专门根据不同的环境，比如说内部环境和外网环境来进行各项配置的单例类。比如说根据内外网环境不同配置不同的baseUrl和appID等等等等。。。。</p>
<pre><code class="copyable">import 'env.dart';

class Config &#123;
  //各种配置
  String APP_ID;
  String SECURITY_KEY;
  String API_DOMAIN;

  // 内网环境
  static final String _NEIBU_APP_ID = "001";
  static final String _NEIBU_SECURITY_KEY = "c5d1c2f4ae7c4c3ba705e6002d51bd92";
  static final String _NEIBU_API_DOMAIN = "https://mobi.neibu.ku.com";
  // 外网环境
  static final String _PRODUCT_APP_ID = "002";
  static final String _PRODUCT_SECURITY_KEY = "d88b5b5d293d418abac9b0627b0ab5a8";
  static final String _PRODUCT_API_DOMAIN = "https://mobi.ku.com";
  void setEnv(Env env)&#123;
    switch (env) &#123;
      case Env.NEIBU:
        APP_ID=_NEIBU_APP_ID;
        SECURITY_KEY=_NEIBU_SECURITY_KEY;
        API_DOMAIN=_NEIBU_API_DOMAIN;
        break;
      case Env.PRODUCT:
        APP_ID=_PRODUCT_APP_ID;
        SECURITY_KEY=_PRODUCT_SECURITY_KEY;
        API_DOMAIN=_PRODUCT_API_DOMAIN;
        break;
      default:
        APP_ID=_PRODUCT_APP_ID;
        SECURITY_KEY=_PRODUCT_SECURITY_KEY;
        API_DOMAIN=_PRODUCT_API_DOMAIN;
        break;
    &#125;
  &#125;


  // 单例对象
  static final Config _instance=Config._internal();
  // 内部构造方法，可避免外部暴露构造函数，进行实例化
  Config._internal();
  // 工厂构造方法，这里使用命名构造函数方式进行声明
  factory Config.getInstance() => _instance;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>env.dart</li>
</ul>
<p>一个标识环境的枚举类</p>
<pre><code class="copyable">enum Env &#123;
  NEIBU,
  PRODUCT
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Utils.dart</li>
</ul>
<p>一个设置公共请求头的类</p>
<pre><code class="copyable">import 'package:fluttertoast/fluttertoast.dart';
class Utils&#123;
  static Map<String,String> getHeader()&#123;
    try &#123;
      return &#123;
      "screensize":"1080*2460",
      "curAppid":"381",
      "channel":"guanfang",
      "User-Agent":"Mozilla/5.0 (Linux; Android 10; V1836A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36",
      "version":"3.3.0",
      "vcode":"330",
      "macaddr":"02:00:00:00:00:00",
    "platform":"android_phone_10",
    "pversion":"1.1",
    "appname":"itspro",
    "vendor":"itspro",
    "imei":"3bc5003ba2ab47c0",
    "model":"vivo,V1836A",
    "Content-Type":"application/x-www-form-urlencoded",
    "Content-Length":"61",
    "Host":"mobi.neibu.ku.com",
    "Connection":"Keep-Alive",
    "Accept-Encoding":"gzip",
      &#125;;
    &#125; catch (exception) &#123;
      toast(exception.toString());
    &#125;
  &#125;

  //static toast(String message) &#123;
    //Fluttertoast.showToast(
      //msg: message,
      //toastLength: Toast.LENGTH_SHORT,
      //gravity: ToastGravity.CENTER,
    //);
  //&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过以上配置，我们就可以在dart中进行愉快地网络请求了。</p></div>  
</div>
            