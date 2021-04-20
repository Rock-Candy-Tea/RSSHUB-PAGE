
---
title: 'Flutter开发总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8c762c331a541cda20c5cc9201a49d8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Apr 2021 01:00:37 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8c762c331a541cda20c5cc9201a49d8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8c762c331a541cda20c5cc9201a49d8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>使用Flutter一直是拒绝的，感觉追不动新技术了。但是当看到用的人越来越多，flutter的书籍已经全面超过OC和Swift了。是时候低下还有几许青丝的头了，虽然学不精，但我学的广。!_!</p>
<h1 data-id="heading-0">一、准备工作</h1>
<p>找一些网上的免费资料学起来，<a href="https://flutterchina.club/widgets/basics/" target="_blank" rel="nofollow noopener noreferrer">flutter中文网站</a>看一个大概，一般感觉看不下去，先看个大概吧。然后详细的学习<a href="https://book.flutterchina.club/" target="_blank" rel="nofollow noopener noreferrer">Flutter实战</a>，将所有的代码都敲一遍。做到所有的功能自己实现。
建议使用Mac来开发，那么<a href="https://flutter.cn/docs/get-started/install" target="_blank" rel="nofollow noopener noreferrer">搭建环境</a>会比较方便。Flutter使用Stable Channel，直接上最新的版本，虽然有一点坑，碰到问题后网上的解决方法有点少。但是办法总比困难多，学习的太顺利，记住的东西太少。
<a href="https://www.dartcn.com/guides/language/language-tour" target="_blank" rel="nofollow noopener noreferrer">Dart语言</a>的学习感觉花一点时间过一下就好，简单的定义变量，函数，集合看一下，够用。</p>
<h1 data-id="heading-1">二、安装及升级</h1>
<p><em>注意：</em>/Public/Flutter/flutter是我本地的路径，需要替换。</p>
<ol>
<li>参考<a href="https://flutter.dev/community/china%E4%B8%8A%E7%9A%84%E6%8F%8F%E8%BF%B0%EF%BC%8C%E5%B0%86flutter%E4%BB%8E%E4%B8%8B%E8%BD%BD%E5%88%B0%E6%9C%AC%E5%9C%B0%E3%80%82%60git" target="_blank" rel="nofollow noopener noreferrer">flutter.dev/community/c…</a> clone -b stable <a href="https://github.com/flutter/flutter.git%60" target="_blank" rel="nofollow noopener noreferrer">github.com/flutter/flu…</a></li>
<li>执行<code>flutter doctor</code>进行dart SDK的下载。</li>
<li><code>vim .bash_profile</code>中添加<code>export PATH=~/Public/Flutter/flutter/bin:$PATH</code>。</li>
<li><code>source .bash_profile</code> 让PATH生效。</li>
<li>在android studio和VS code安装flutter插件。</li>
<li><code>flutter upgrade</code> 在/Users/arthurwang/Public/Flutter/flutter 安装flutter路径中进行。</li>
</ol>
<h1 data-id="heading-2">三、 常用布局</h1>
<ol>
<li>Container： 只有一个子Widget。默认充满，包含了padding、margin、color、宽高、decoration等。</li>
<li>Padding： 只有一个子Widget。只用于设置Padding，常用于嵌套child，给child设置padding。</li>
<li>Center：只有一个子Widget。只用于居中显示，常用于嵌套child，给child设置居中。</li>
<li>Stack：可以有多个子Widget。子Widget堆叠在一起。</li>
<li>Column：可以有多个子Widget。垂直布局。</li>
<li>Row： 可以有多个子Widget。水平布局。</li>
<li>Expanded：只有一个子Widget。在Column和Row中充满。（不会超出父视图）</li>
<li>ListView：可以有多个子Widget。</li>
<li>Align: 只有一个子Widget。 绝对布局，可以设置位置。</li>
<li>SizeBox： 强制设置它的孩子宽度或者高度为指定值。传width、height、child。</li>
</ol>
<p>明白这些布局的使用，基本能够满足页面的布局。</p>
<h1 data-id="heading-3">四、组件</h1>
<ol>
<li>MaterailApp：作为APP顶层的主要入口，可配置主题，多语言，路由等。</li>
<li>Scaffold： 用户页面承载Widget，包含appbar、snackbar、drawer等material design设定。</li>
<li>AppBar： 用于Scaffold的appbar，内有标题、二级页面返回按键等。</li>
<li>Text：显示文本，可通过style设置TextStyle来设置字体样式等。</li>
<li>RichText： 福文本。设置TextSpan，可以拼接出富文本场景。</li>
<li>TextField： 文本输入框。</li>
<li>Image： 图片加载。</li>
<li>FlatButton： 按键点击。</li>
</ol>
<p>明白基本组件，可以构建一般页面了。</p>
<h1 data-id="heading-4">五、 网络请求</h1>
<p>有两种思路（1）通过flutter和native交互，发送url和params到native，然后返回结果。（2）通过flutter和native交互，从native获取params然后在flutter进行网络请求。
考虑到Android的网络第三方库使用注解来实现请求，所以放弃了思路（1），尝试思路（2）并封装请求。
网络请求官方推荐第三方库<a href="https://pub.dev/packages/dio" target="_blank" rel="nofollow noopener noreferrer">Dio</a>。</p>
<pre><code class="copyable">
class ApiService &#123;
  // 单例配置
  static ApiService get apiService => _getInstance();
  static ApiService _apiService = ApiService._internal();

  // 网络请求配置
  static const _platform = const MethodChannel("******");
  static Dio _dio = Dio();

  String? _baseUrl;
  static const int _GET = 0;
  static const int _POST = 1;

  // 初始化
  factory ApiService() => _getInstance();

  static ApiService _getInstance() &#123;
    return _apiService;
  &#125;

  ApiService._internal() &#123;
    _dio.options.connectTimeout = 5000;
    _dio.options.receiveTimeout = 3000;
    _dio.options.contentType = Headers.formUrlEncodedContentType;
    _dio.options.responseType = ResponseType.json;

    _setBaseUrl();
  &#125;

  Future<void> _setBaseUrl() async &#123;
    try &#123;
      String? baseUrl = await _platform.invokeMethod("***") as String?;
      if (null != baseUrl) &#123;
        _dio.options.baseUrl = baseUrl;
        _baseUrl = baseUrl;
      &#125;
    &#125; on PlatformException catch (e) &#123;
      // Do nothing
    &#125;
  &#125;

  Future<Map<String, dynamic>?> _request(
      int type, String url, Map<String, String>? params) async &#123;
    if (null == _baseUrl) &#123;
      await _setBaseUrl();
    &#125;

    Map<String, String>? tokenParams;
    try &#123;
      Map<String, String>? paramsMap;
      if (null != params) &#123;
        paramsMap = Map();
        paramsMap["params"] = json.encode(params);
      &#125;

      tokenParams = Map<String, String>.from(
          await _platform.invokeMethod("***", paramsMap));
    &#125; on PlatformException catch (e) &#123;
      // Do nothing
    &#125;

    print("ApiService url is $url, params is $tokenParams");

    Response<Map<String, dynamic>>? response;
    try &#123;
      switch (type) &#123;
        case _GET:
          response = await _dio.get(url, queryParameters: tokenParams);
          break;

        case _POST:
          response = await _dio.post(url, queryParameters: tokenParams);
          break;
      &#125;
    &#125; on DioError catch (e) &#123;
      print("$url 错误 $&#123;e.message&#125;");
      throw RequestError(kUnknownError, "服务器走失了，请稍后重试");
    &#125;

    print("$url response is $response");

    if (0 != response?.data?["status"]) &#123;
      throw RequestError(response?.data?["status"], response?.data?["msg"]);
    &#125; else &#123;
      print("ApiService response.data is $&#123;response?.data&#125;");
      return response?.data;
    &#125;
  &#125;

  // 网络请求

  // 获取信息
  Future<UserInfoEntity> getUserInfo() async &#123;
    Map<String, dynamic>? response =
        await _request(_GET, "url/url/url", null);

    if (null != response) &#123;
      return UserInfoEntity().fromJson(response);
    &#125; else &#123;
      throw RequestError(kUnknownError, "服务器走失了，请稍后重试");
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>采用工厂模式创建一个网络请求，在创建时设置好配置。之后添加新的接口，只需要在底部依次添加。</p>
<pre><code class="copyable"> Future<UserInfoEntity> getUserInfo() async &#123;
    Map<String, dynamic>? response =
        await _request(_GET, "url/url/url", null);

    if (null != response) &#123;
      return UserInfoEntity().fromJson(response);
    &#125; else &#123;
      throw RequestError(kUnknownError, "服务器走失了，请稍后重试");
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>采用处</p>
<pre><code class="copyable">try &#123;
      UserInfoEntity entity = await ApiService.apiService.getUserInfo();
      userInfoData = entity.data;
      notifyListeners();
    &#125; on RequestError catch (e) &#123;
      print("e.message is $&#123;e.message&#125;, e.code is $&#123;e.code&#125;");
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中的UserInfoEntity为定义的Model，RequestError为自定错误类型。</p>
<h1 data-id="heading-5">六、 Json转Model</h1>
<p>强烈推荐Android Studio的插件FlutterJsonBeanFactory，使用方法参照官网。如果要修改或重建Model，那么将之前的model删除再创建一次。有一些小的修改，可以用alt+J来刷新。
*注意：*Json数据如果不能“Make”，那么可以试下将最后一个逗号删除。</p>
<h1 data-id="heading-6">七、 状态共享</h1>
<p>当用户信息此数据需要用在很多页面，那么考虑采用官方推荐的<a href="https://pub.dev/packages/provider" target="_blank" rel="nofollow noopener noreferrer">provider</a>来实现刷新Widget。</p>
<pre><code class="copyable">void main() => runApp(ChangeNotifierProvider<PersonalCenterProviderModel>.value(
      value: PersonalCenterProviderModel(),
      child: MyApp(),
    ));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>建议将Provider添加到顶部，方便在任何页面中获取UserInfo。</p>
<pre><code class="copyable">class PersonalCenterProviderModel with ChangeNotifier &#123;
  UserInfoData? userInfoData;

  void refreshUserInfo() async &#123;
    try &#123;
      UserInfoEntity entity = await ApiService.apiService.getUserInfo();
      userInfoData = entity.data;
      notifyListeners();
    &#125; on RequestError catch (e) &#123;
      print("e.message is $&#123;e.message&#125;, e.code is $&#123;e.code&#125;");
    &#125;
  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>PersonalCenterProviderModel类中可以添加很多方法来更新数据。</p>
<pre><code class="copyable">PersonalCenterProviderModel _model =
        Provider.of<PersonalCenterProviderModel>(context);
backgroundImage: NetworkImage(_model.userInfoData?.portrait ?? defaultImage),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用方式，当userInfo中的portrait发生改变时，那么页面会重建。</p>
<pre><code class="copyable">PersonalCenterProviderModel _model =
      Provider.of<PersonalCenterProviderModel>(context, listen: false);
      _model.refreshUserInfo();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果仅仅是获取model来调用方法，那么将listen设置为false。</p>
<h1 data-id="heading-7">八、Flutter和Native交互</h1>
<p>参考<a href="https://flutter.cn/docs/development/add-to-app/ios/project-setup" target="_blank" rel="nofollow noopener noreferrer">module集成</a>到iOS和Android。
iOS的使用方式</p>
<pre><code class="copyable">- (void)initialFlutterVC
&#123;
    FlutterEngine *flutterEngine = [[FlutterEngine alloc] initWithName:@"my flutter engine"];
    [flutterEngine run];
    [GeneratedPluginRegistrant registerWithRegistry:flutterEngine];
    self.flutterViewController = [[FlutterViewController alloc] initWithEngine:flutterEngine nibName:nil bundle:nil];
    [self initialFlutterMethods];
    
    self.flutterViewController.modalPresentationStyle = UIModalPresentationFullScreen;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开Flutter页面</p>
<pre><code class="copyable">- (void)personalButtonDidClick:(id)sender
&#123;
    [self presentViewController:self.flutterViewController animated:YES completion:nil];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>记得提前初始化flutterEngine，可以加快打开的速度。
Android的使用方式</p>
<pre><code class="copyable">flutterEngine = new FlutterEngine(this);
        flutterEngine.getDartExecutor().executeDartEntrypoint(DartExecutor.DartEntrypoint.createDefault());
        FlutterEngineCache.getInstance().put(engine_personal_center, flutterEngine);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提前初始化flutterEngine</p>
<pre><code class="copyable">btn_jump.setOnClickListener(new View.OnClickListener() &#123;
            @Override
            public void onClick(View v) &#123;
                startActivity(FlutterActivity.
                        withCachedEngine(engine_personal_center).build(HomeActivity.this));
            &#125;
        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过缓存打开Flutter页面。</p>
<p>添加交互方法</p>
<pre><code class="copyable">final String CHANNEL = "*";
        MethodChannel methodChannel = new MethodChannel(flutterEngine.getDartExecutor().getBinaryMessenger(), CHANNEL);
        methodChannel.setMethodCallHandler(new MethodChannel.MethodCallHandler() &#123;
            @Override
            public void onMethodCall(@NonNull MethodCall call, @NonNull MethodChannel.Result result) &#123;
                switch (call.method) &#123;
                    case "*":
                        result.success(API.SERVER_URL);
                        break;
                    case "*":
                        String paramsStr = call.argument("params");
                        Gson gson = new Gson();
                        Type jsonType = new TypeToken<HashMap<String, String>>() &#123;
                        &#125;.getType();
                        HashMap<String, String> params = gson.fromJson(paramsStr, jsonType);
                        result.success(ParamManager.Companion.token(params));
                        break;
                    case "*":
                        EventMessage<String> eventMessage = new EventMessage<>();
                        eventMessage.setTag(EVENT_LOGOUT);
                        EventBus.getDefault().post(eventMessage);

                        UserAccount.getInstance().logout();

                        break;

                    case "*":
                        String path = call.argument("imagePath");
                        if (null == path || path.isEmpty()) &#123;
                            result.error("1", "上传失败", null);
                        &#125; else &#123;
                            uploadImageToOSS(path, result);
                        &#125;

                        break;

                    case "*":
                        // DO Nothing
                        break;
                    default:
                        result.notImplemented();
                        break;
                &#125;
            &#125;
        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>iOS与Android的用法类似，<em>注意</em>必须是同一个flutterEngine，不然会找不到。</p>
<h1 data-id="heading-8">九、iOS打包</h1>
<p>如果打包的证书不是debug或release，那么需要FLUTTER_BUILD_MODE设置为Release才能进行Ad-hoc和Release打包。
在../qiji_flutter/.ios/Flutter/flutter_export_environment.sh中添加
<code>export "FLUTTER_BUILD_MODE=Release"</code>。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            