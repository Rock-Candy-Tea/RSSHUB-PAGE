
---
title: 'Flutter 仿写新闻客户端'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e78ad2251b0a478583454fdbf0533e94~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Fri, 12 Aug 2022 06:09:17 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e78ad2251b0a478583454fdbf0533e94~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>携手创作，共同成长！这是我参与「掘金日新计划 · 8 月更文挑战」的第17天，<a href="https://juejin.cn/post/7123120819437322247" target="_blank" title="https://juejin.cn/post/7123120819437322247">点击查看活动详情</a></p>
<h3 data-id="heading-0">新建项目，加入图片字体，编写欢迎界面</h3>
<p><strong>新建项目</strong></p>
<p><code>flutter create jimmy_flutter_demo</code></p>
<p><strong>加入图片字体</strong></p>
<p>在根目录上新建一个 <code>assets</code> 文件夹</p>
<pre><code class="hljs language-bash copyable" lang="bash">assets
  fonts // 存放字体
  images // 存放图片
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>pubspec.yaml</code> 文件设定 <code>images</code> 的路径内容：</p>
<pre><code class="hljs language-bash copyable" lang="bash">assets:
  - assets/images/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>pubspec.yaml</code> 文件设定 <code>fonts</code> 的路径内容：</p>
<pre><code class="hljs language-bash copyable" lang="bash">fonts:
  - family: Avenir
    fonts:
      - asset: assets/fonts/Avenir-Book.ttf
        weight: 400
  - family: Montserrat
    fonts:
      - asset: assets/fonts/Montserrat-SemiBold.ttf
        weight: 600
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>编写欢迎页面</strong></p>
<p>添加屏幕适配的包。</p>
<pre><code class="hljs language-bash copyable" lang="bash">  <span class="hljs-comment"># 屏幕适配</span>
  flutter_screenutil: ^1.0.2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拉取新包：<code>flutter pub get</code> 获取直接安装 <code>flutter pub add flutter_screenutil</code>。</p>
<p>设定屏幕见 <code>lib/common/utils/screen.dart</code>。</p>
<p>设定这个 <code>app</code> 的一些色调，见 <code>lib/common/values/colors.dart</code></p>
<p>添加欢迎页面 <code>lib/pages/welcome/welcomePage.dart</code></p>
<p>更改入口文件 <code>lib/main.dart</code></p>
<pre><code class="hljs language-bash copyable" lang="bash">import <span class="hljs-string">'package:flutter/material.dart'</span>;
import <span class="hljs-string">'package:flutter_screenutil/flutter_screenutil.dart'</span>;
import <span class="hljs-string">'package:jimmy_flutter_demo/pages/welcome/welcomePage.dart'</span>;

void main() => runApp(MyApp());

// 查看 https://github.com/OpenFlutter/flutter_screenutil/blob/master/README_CN.md

class MyApp extends StatelessWidget &#123;
  @override
  Widget build(BuildContext context) &#123;
    //填入设计稿中设备的屏幕尺寸,单位dp
    <span class="hljs-built_in">return</span> ScreenUtilInit(
      designSize: const Size(360, 690),
      minTextAdapt: <span class="hljs-literal">true</span>,
      splitScreenMode: <span class="hljs-literal">true</span>,
      builder: (context, child) &#123;
        <span class="hljs-built_in">return</span> MaterialApp(
          debugShowCheckedModeBanner: <span class="hljs-literal">false</span>,
          title: <span class="hljs-string">'First Method'</span>,
          theme: ThemeData(
            primarySwatch: Colors.blue,
            textTheme: Typography.englishLike2018.apply(fontSizeFactor: 1.sp),
          ),
          home: child,
        );
      &#125;,
      child: const WelcomePage(),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里需要对 <code>flutter_screenutil</code> 做全局的引入。</p>
</blockquote>
<p>然后对欢迎页面进行添加，内容如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash">import <span class="hljs-string">'package:flutter/material.dart'</span>;
import <span class="hljs-string">'package:jimmy_flutter_demo/common/utils/utils.dart'</span>;
import <span class="hljs-string">'package:jimmy_flutter_demo/common/values/values.dart'</span>;

class WelcomePage extends StatelessWidget &#123;
  const WelcomePage(&#123;Key? key&#125;) : super(key: key);

  // 页头标题
  Widget <span class="hljs-function"><span class="hljs-title">_buildPageHeaderTitle</span></span>() &#123;
    <span class="hljs-built_in">return</span> Container(
      margin: EdgeInsets.only(top: duSetHeight(65)),
      child: Text(
        <span class="hljs-string">"Features"</span>,
        textAlign: TextAlign.center,
        style: TextStyle(
          color: AppColors.primaryText,
          fontFamily: <span class="hljs-string">"Montserrat"</span>,
          fontWeight: FontWeight.w600,
          fontSize: duSetFontSize(24),
        ),
      ),
    );
  &#125;

  // 页头说明
  Widget <span class="hljs-function"><span class="hljs-title">_buildPageHeaderDetail</span></span>() &#123;
    <span class="hljs-built_in">return</span> Container(
      width: duSetWidth(242),
      height: duSetHeight(70),
      margin: EdgeInsets.only(top: duSetHeight(14)),
      child: Text(
        <span class="hljs-string">"The best of news channels all in one place. Trusted sources and personalized news for you."</span>,
        textAlign: TextAlign.center,
        style: TextStyle(
          color: AppColors.primaryText,
          fontFamily: <span class="hljs-string">"Avenir"</span>,
          fontWeight: FontWeight.normal,
          fontSize: duSetFontSize(16),
          height: 1.3,
        ),
      ),
    );
  &#125;

  // 特性说明
  // 宽度 80 + 20 + 195 = 295
  Widget _buildFeatureItem(String imageName, String intro, double marginTop) &#123;
    <span class="hljs-built_in">return</span> Container(
      width: duSetWidth(295),
      height: duSetHeight(80),
      margin: EdgeInsets.only(top: duSetHeight(marginTop)),
      child: Row(
        children: [
          Container(
            width: duSetWidth(80),
            height: duSetHeight(80),
            child: Image.asset(
              <span class="hljs-string">"assets/images/<span class="hljs-variable">$imageName</span>.png"</span>,
              fit: BoxFit.none,
            ),
          ),
          const Spacer(),
          Container(
            width: duSetWidth(195),
            child: Text(
              intro,
              textAlign: TextAlign.center,
              style: TextStyle(
                color: AppColors.primaryText,
                fontFamily: <span class="hljs-string">"Avenge"</span>,
                fontWeight: FontWeight.normal,
                fontSize: duSetFontSize(16),
              ),
            ),
          ),
        ],
      ),
    );
  &#125;

  // 开始按钮
  Widget <span class="hljs-function"><span class="hljs-title">_buildStartButton</span></span>() &#123;
    <span class="hljs-built_in">return</span> Container(
      width: duSetWidth(295),
      height: duSetHeight(44),
      margin: EdgeInsets.only(bottom: duSetHeight(20)),
      child: TextButton(
        onPressed: () => &#123;&#125;,
        style: ButtonStyle(
          backgroundColor: MaterialStateProperty.all(AppColors.primaryElement),
          textStyle: MaterialStateProperty.all(const TextStyle(
            color: AppColors.primaryElementText,
          )),
        ),
        child: const Text(<span class="hljs-string">"Get started"</span>),
      ),
    );
  &#125;

  @override
  Widget build(BuildContext context) &#123;
    <span class="hljs-built_in">return</span> Scaffold(
      body: Center(
        child: Column(
          children: <Widget>[
            _buildPageHeaderTitle(),
            _buildPageHeaderDetail(),
            _buildFeatureItem(
              <span class="hljs-string">"feature-1"</span>,
              <span class="hljs-string">"Compelling photography and typography provide a beautiful reading"</span>,
              86,
            ),
            _buildFeatureItem(
              <span class="hljs-string">"feature-2"</span>,
              <span class="hljs-string">"Sector news never shares your personal data with advertisers or publishers"</span>,
              40,
            ),
            _buildFeatureItem(
              <span class="hljs-string">"feature-3"</span>,
              <span class="hljs-string">"You can get Premium to unlock hundreds of publications"</span>,
              40,
            ),
            const Spacer(),
            _buildStartButton()
          ],
        ),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>上面的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fapi.flutter.dev%2Fflutter%2Fmaterial%2FTextButton-class.html" target="_blank" rel="nofollow noopener noreferrer" title="https://api.flutter.dev/flutter/material/TextButton-class.html" ref="nofollow noopener noreferrer">TextButton</a> 本来使用的是 FlatButton， 但是它已经被弃用了。</p>
</blockquote>
<p>相关的效果图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e78ad2251b0a478583454fdbf0533e94~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="第一课效果图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">静态路由，组件抽取，登陆注册页面</h3>
<p>为了实现静态路由，我们来定义下登陆和注册的页面：</p>
<ul>
<li>登录页 lib/pages/sign_in/sign_in.dart</li>
<li>注册页 lib/pages/sign_up/sign_up.dart</li>
<li>静态路由 lib/routes.dart</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">// 登陆页面初始化
import <span class="hljs-string">'package:flutter/material.dart'</span>;

class SignInPage extends StatelessWidget &#123;
  SignInPage(&#123;Key? key&#125;) : super(key: key);

  @override
  Widget build(BuildContext context) &#123;
    <span class="hljs-built_in">return</span> Scaffold(
      body: Center(
        child: Column(
          children: <Widget>[
            Text(<span class="hljs-string">'Sign In'</span>),
            Text(<span class="hljs-string">'Hello'</span>),
            Text(<span class="hljs-string">'World'</span>),
          ],
        ),
      ),
    );
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash">// 注册页面初始化
import <span class="hljs-string">'package:flutter/material.dart'</span>;

class SignUpPage extends StatelessWidget &#123;
  SignUpPage(&#123;Key? key&#125;) : super(key: key);

  @override
  Widget build(BuildContext context) &#123;
    <span class="hljs-built_in">return</span> Scaffold(
      body: Center(
        child: Column(
          children: <Widget>[
            Text(<span class="hljs-string">'Sign Up'</span>),
            Text(<span class="hljs-string">'Hello'</span>),
            Text(<span class="hljs-string">'World'</span>),
          ],
        ),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash">// 路由信息
import <span class="hljs-string">'package:jimmy_flutter_demo/pages/sign_in/sign_in.dart'</span>;
import <span class="hljs-string">'package:jimmy_flutter_demo/pages/sign_up/sign_up.dart'</span>;

// 静态路由
var staticRoutes = &#123;
  <span class="hljs-string">"/sign-in"</span>: (context) => SignInPage(), // 登录
  <span class="hljs-string">"/sign-up"</span>: (context) => SignUpPage(), // 注册
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装使用 <code>fluttertoast</code> 报错的解决：</p>
<pre><code class="hljs language-bash copyable" lang="bash">[Parse Issue (Xcode): Module <span class="hljs-string">'fluttertoast'</span> not found
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决方案:</p>
<pre><code class="hljs language-bash copyable" lang="bash">1.  进入项目 ios 文件夹，删除文件  **<span class="hljs-string">"Podfile"</span>**  和  **<span class="hljs-string">"Podfile. Lock"</span>**  
2.  ios 目录下，在终端执行 `flutter clean` 命令行
3.  回到项目根目录，在终端执行 `flutter pub get`
4.  ios 目录下，在终端执行 `pod install` 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>组件 appBar 拆分过程的报错：<code>The argument type 'Widget' can't be assigned to the parameter type 'PreferredSizeWidget?'</code></strong></p>
<p>解决方案：</p>
<pre><code class="hljs language-bash copyable" lang="bash">因为我们定义了 appBar 组件是 `Widget`，我们应该定义其为 `PreferredSizeWidget`。

Widget transparentAppBar(&#123;
  required BuildContext context,
  required List<Widget> actions,
&#125;) &#123;&#125;

// 改为

PreferredSizeWidget transparentAppBar(&#123;
  required BuildContext context,
  required List<Widget> actions,
&#125;) &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>组件抽取</strong></p>
<p>比如: toast</p>
<pre><code class="hljs language-bash copyable" lang="bash">import <span class="hljs-string">'dart:ui'</span>;

import <span class="hljs-string">'package:flutter/material.dart'</span>;
import <span class="hljs-string">'package:jimmy_flutter_demo/common/utils/utils.dart'</span>;
import <span class="hljs-string">'package:fluttertoast/fluttertoast.dart'</span>;

Future toastInfo(&#123;
  required String msg,
  Color backgroundColor = Colors.black,
  Color textColor = Colors.white,
&#125;) async &#123;
  <span class="hljs-built_in">return</span> await Fluttertoast.showToast(
    msg: msg,
    toastLength: Toast.LENGTH_SHORT,
    gravity: ToastGravity.TOP,
    timeInSecForIosWeb: 1,
    backgroundColor: backgroundColor,
    textColor: textColor,
    fontSize: duSetFontSize(16),
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>又比如：appBar</p>
<pre><code class="hljs language-bash copyable" lang="bash">import <span class="hljs-string">'package:flutter/material.dart'</span>;
import <span class="hljs-string">'package:jimmy_flutter_demo/common/values/values.dart'</span>;

// 透明背景的 AppBar
PreferredSizeWidget transparentAppBar(&#123;
  // 使用 PreferredSizeWidget 定义，而不是 Widget
  required BuildContext context,
  required List<Widget> actions,
&#125;) &#123;
  <span class="hljs-built_in">return</span> AppBar(
    backgroundColor: Colors.transparent,
    elevation: 0,
    title: const Text(<span class="hljs-string">''</span>),
    leading: IconButton(
      icon: const Icon(
        Icons.arrow_back,
        color: AppColors.primaryText,
      ),
      onPressed: () &#123;
        Navigator.pop(context);
      &#125;,
    ),
    actions: actions,
  );
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">Dio 的封装使用</h3>
<ol>
<li>处理报错：<code>Non-nullable instance field '_storage' must be initialized.\ Try adding an initializer expression, or add a field initializer in this constructor, or mark it 'late'.</code></li>
</ol>
<p>解决方案，在变量 <code>_storage</code> 添加 <code>late</code> 修饰符。</p>
<ol start="2">
<li>处理报错 <code>The argument type 'void Function(RequestOptions)' can't be assigned to the parameter type 'void Function(RequestOptions, RequestInterceptorHandler)?'</code> 封装 <code>dio</code> 的时候出现。</li>
</ol>
<p>解决方案，可以尝试方法如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-function"><span class="hljs-title">initializeInterceptor</span></span>()&#123;
    _dio.interceptors.add(InterceptorsWrapper(
        onError: (error, errorInterceptorHandler )&#123;
          <span class="hljs-built_in">print</span>(error.message);
        &#125;,
        onRequest: (request, requestInterceptorHandler)&#123;
          <span class="hljs-built_in">print</span>(<span class="hljs-string">"<span class="hljs-variable">$&#123;request.method&#125;</span> | <span class="hljs-variable">$&#123;request.path&#125;</span>"</span>);
        &#125;,
        onResponse: (response, responseInterceptorHandler) &#123;
          <span class="hljs-built_in">print</span>(<span class="hljs-string">'$&#123;response.statusCode&#125; $&#123;response.statusCode&#125; $&#123;response.data&#125;'</span>);
        &#125;
    ));
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后续更新...</p>
<h3 data-id="heading-3">往期精彩推荐</h3>
<ul>
<li><a href="https://juejin.cn/post/7124839733280112671" target="_blank" title="https://juejin.cn/post/7124839733280112671">Dart 知识点 - 数据类型</a></li>
<li><a href="https://juejin.cn/post/7126173613035618335" target="_blank" title="https://juejin.cn/post/7126173613035618335">Flutter 开发出现的那些 Bugs 和解决方案「持续更新... 」</a></li>
</ul>
<p>如果读者觉得文章还可以，不防一键三连：关注➕点赞➕收藏</p></div>  
</div>
            