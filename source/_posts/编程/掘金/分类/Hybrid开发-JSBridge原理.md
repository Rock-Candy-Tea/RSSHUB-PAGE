
---
title: 'Hybrid开发-JSBridge原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea069b0974854fb6849f0db2b1309099~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 00:26:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea069b0974854fb6849f0db2b1309099~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Hybrid混合开发相对于单一的客户端开发有着开发周期短，迭代快的优势，但是Hybrid模式开发的页面存在着一定的缺陷，比如性能问题、缺乏客户端能力等。通过JSBridge这个桥梁可以实现客户端能力的打通，赋予了Hybrid应用更强的端能力。<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Ficantunderstand.cn%2F2021%2F07%2F07%2FJsBridge%2FJSBridge.jpg" target="_blank" rel="nofollow noopener noreferrer" title="https://icantunderstand.cn/2021/07/07/JsBridge/JSBridge.jpg" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea069b0974854fb6849f0db2b1309099~tplv-k3u1fbpfcp-zoom-1.image" alt="JS" loading="lazy" referrerpolicy="no-referrer"></a><br>
JSBridge作为客户端和H5的通信的桥梁，可以承接如下的能力:</p>
<ul>
<li>鉴权能力 JSBridge调用能力鉴权，白名单，黑名单等</li>
<li>胶水能力 JSBridge兼容代码，做版本控制等调用透明</li>
<li>测试能力 提供测试方法，方便测试</li>
<li>Scope(配置)能力 能基于配置产出精简版、目标版本JSBridge</li>
</ul>
<p>下面以Android代码为例，介绍JSBridge的实现方式。</p>
<h2 data-id="heading-0">Js调用Native</h2>
<p>Js调用Native通常有如下的方案:</p>
<ul>
<li>拦截请求(shouldOverrideUrlLoading/shouldInterceptRequest)</li>
<li>拦截特定方法(prompt/alert/confirm)</li>
<li>客户端注入JSBridge(addJavascriptInterface)</li>
</ul>
<h3 data-id="heading-1">拦截请求</h3>
<p>在安卓初始化Wevview的时候可以设定WebViewClient，WebViewClient主要功能是处理Webview加载时的通知和请求事件等。通过重写WebViewClient的shouldOverrideUrlLoading/shouldInterceptRequest就可以实现拦截h5的请求从而实现端能力调用。<br>
实现思路如下:</p>
<ul>
<li>定义JSBridge实现Jsb方法</li>
<li>定义JSBManager管理Jsb的调用</li>
<li>实现拦截方法的重写</li>
<li>H5侧调用</li>
</ul>
<h4 data-id="heading-2">定义JSBridge方法类</h4>
<pre><code class="copyable">// 以下例子均省略import语句 
public class JSBridge &#123;
  // 需要考虑callback和入参一致性问题
  public void showToast(JSONObject jsonObject) &#123;
      try &#123;
          Toast.makeText(MainActivity.context, jsonObject.getString("content"), Toast.LENGTH_LONG).show();
      &#125; catch(Exception e) &#123;
      &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">定义JSBManager管理Jsb的调用</h4>
<pre><code class="copyable">public class JsbManager &#123;
  // 通过HashMap获取JSBridge定义的所有方法
  public static Map<String, Method> methodMap = new HashMap<>();
  public void init() &#123;
      Method[] methods = JSBridge.class.getDeclaredMethods();
      for(Method method : methods) &#123;
          methodMap.put(method.getName(), method);
      &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">实现拦截方法的重写</h4>
<p>以下以shouldOverrideUrlLoading方法的重写为例子。在例子中定义的通信协议是myjsb://method?params。通过在拦截方法中对请求进行解析就可以实现调用对应客户端method的逻辑。</p>
<pre><code class="copyable">public class CustomWebViewClient extends WebViewClient &#123;
    private JsbManager jsbManager = new JsbManager();
    private JSBridge jsBridge = new JSBridge();
    public void initJsb() &#123;
        // 初始jsbManager和jsBridge实例
        jsbManager.init();
        jsBridge = new JSBridge();
    &#125;
    @Override
    public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) &#123;
        // 处理jsb 协议情况  只拦截jsb协议的url 其他放行
        Uri uri = request.getUrl();
        String scheme = uri.getScheme();
        if(scheme.equals(new String("myjsb"))) &#123;
            // 获取方法名 入参
            String methodName = uri.getAuthority();
            String query = uri.getQuery();
            try &#123;
                JSONObject jsonObject = new JSONObject(query);
                Method method = jsbManager.methodMap.get(methodName);
                // 调用对应的客户端逻辑
                method.invoke(jsBridge,jsonObject);
            &#125; catch(Exception e) &#123;
                e.printStackTrace();
            &#125;
        &#125;
        return super.shouldOverrideUrlLoading(view, request);
    &#125;
&#125;
// 主活动代码逻辑
public class MainActivity extends AppCompatActivity &#123;
    @Override
    protected void onCreate(Bundle savedInstanceState) &#123;
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // 创建WebViewClient
        CustomWebViewClient webViewClient = new CustomWebViewClient();
        // 调用JSBridge初始逻辑
        webViewClient.initJsb();
        WebView webView = (WebView) findViewById(R.id.webView);
        // 设置WebViewClient处理webviewt通知，请求等
        webView.setWebViewClient(webViewClient);
        // 开启调试功能
        webView.setWebContentsDebuggingEnabled(true);
        WebSettings webSettings = webView.getSettings();
        // 允许执行JS
        webSettings.setJavaScriptEnabled(true);
        // 这里加载项目本地的html文件方便调试
        webView.loadUrl("file:///android_asset/index.html");
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">H5侧调用</h4>
<pre><code class="copyable">    <body>
        <div>this page test JSB</div>
        <script>
          // 通过创建iframe发起JSBridge调用
          function iframeCall(url) &#123;
            let iframe = document.createElement('iframe')
            iframe.src = url
            iframe.style.display = 'none'
            document.documentElement.appendChild(iframe)
            setTimeout(() => &#123; document.documentElement.removeChild(iframe) &#125;)
          &#125;
          function callJsb(method, params) &#123;
            let url = `myjsb://`
            if(!method) &#123;
              return
            &#125;
            url += `$&#123;method&#125;`
            if(!!params) &#123;
              url += `?$&#123;encodeURIComponent(JSON.stringify(params))&#125;`
            &#125;
            iframeCall(url)
          &#125;
          callJsb('showToast', &#123; content: 'xiaohong' &#125;)
        </script>
    </body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>                                  <a href="https://link.juejin.cn/?target=https%3A%2F%2Ficantunderstand.cn%2F2021%2F07%2F07%2FJsBridge%2FoverrideUrlCall.png" target="_blank" rel="nofollow noopener noreferrer" title="https://icantunderstand.cn/2021/07/07/JsBridge/overrideUrlCall.png" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1f2b403a7bc4b75a38ed596f68b6cee~tplv-k3u1fbpfcp-zoom-1.image" alt="拦截请求实现调用" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>使用iframe发送消息的方式会存在消息丢失，参数限制等问题，可以通过消息队列和拦截shouldInterceptRequest方法来实现。</p>
<h3 data-id="heading-6">拦截特定方法</h3>
<p>在初始化WebView的时候可以同步设置WebChromeClient，WebChromeClient主要是辅助WebView处理Js对话框，标题等操作，通过拦截WebChromeClient相应的方法同样可以实现调用端能力。</p>
<h4 data-id="heading-7">实现WebChromeClient</h4>
<pre><code class="copyable">public class CustomWebChromeClient extends WebChromeClient &#123;
    @Override
    public boolean onJsPrompt(WebView view, String url, String message, String defaultValue, JsPromptResult result) &#123;
        // 此处举例为主 直接弹端toast
        // 实现上跟拦截url一致
        Log.d("mesage", message.startsWith("myjsb")+ "");
        if(message.startsWith("myjsb")) &#123;
            Toast.makeText(MainActivity.context, "PropmtCall", Toast.LENGTH_LONG).show();
            // 此时js调起了 需要JsPromptResult.confirm(result)
            return true;
        &#125; else &#123;
            return super.onJsPrompt(view, url, message, defaultValue, result);
        &#125;
    &#125;
&#125;
// 在初始化WebView的时候设置WebChromeClient
CustomWebChromeClient webChromeClient = new CustomWebChromeClient();
webView.setWebChromeClient(webChromeClient);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">H5调用</h4>
<pre><code class="copyable">    window.prompt('myjsb://')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>                                 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ficantunderstand.cn%2F2021%2F07%2F07%2FJsBridge%2FoverridePrompt.png" target="_blank" rel="nofollow noopener noreferrer" title="https://icantunderstand.cn/2021/07/07/JsBridge/overridePrompt.png" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36a5965aa900431b85bfb3a026417451~tplv-k3u1fbpfcp-zoom-1.image" alt="重写Prompt方法调用" loading="lazy" referrerpolicy="no-referrer"></a></p>
<h3 data-id="heading-9">客户端注入JSBridge</h3>
<p>通过<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fandroid%2Fwebkit%2FWebView%23addJavascriptInterface(java.lang.Object%2C%2520java.lang.String)" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.android.com/reference/android/webkit/WebView#addJavascriptInterface(java.lang.Object,%20java.lang.String)" ref="nofollow noopener noreferrer">addJavascriptInterface</a>可以在初始化WebView的时候将客户端的调用逻辑暴露给H5。</p>
<h4 data-id="heading-10">实现JSInterface</h4>
<pre><code class="copyable">    public class JsInterface &#123;
        private Context context;
        public JsInterface(Context context) &#123;
            this.context = context;
        &#125;
        // JsInterface需要用@JavascriptInterface注解才可以被调用
        @JavascriptInterface
        public void showToast(String content) &#123;
            Toast.makeText(this.context, content, Toast.LENGTH_LONG).show();
        &#125;
    &#125;

    // 在初始WebView的时候注入interface
    webView.addJavascriptInterface(new JsInterface(context), "myjsb");
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">H5调用</h4>
<pre><code class="copyable">    window.myjsb.showToast("Interface")  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>                                   <a href="https://link.juejin.cn/?target=https%3A%2F%2Ficantunderstand.cn%2F2021%2F07%2F07%2FJsBridge%2FcallInterface.png" target="_blank" rel="nofollow noopener noreferrer" title="https://icantunderstand.cn/2021/07/07/JsBridge/callInterface.png" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46b83b282b784e069e78cd9e21a53200~tplv-k3u1fbpfcp-zoom-1.image" alt="interface调用" loading="lazy" referrerpolicy="no-referrer"></a></p>
<h2 data-id="heading-12">Native调用Js</h2>
<p>Nativa调用Js通常有如下的方案:</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fandroid%2Fwebkit%2FWebView%23loadUrl(java.lang.String)" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.android.com/reference/android/webkit/WebView#loadUrl(java.lang.String)" ref="nofollow noopener noreferrer">loadUrl</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fandroid%2Fwebkit%2FWebView%23evaluateJavascript(java.lang.String%2C%2520android.webkit.ValueCallback%253Cjava.lang.String%253E)" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.android.com/reference/android/webkit/WebView#evaluateJavascript(java.lang.String,%20android.webkit.ValueCallback%3Cjava.lang.String%3E)" ref="nofollow noopener noreferrer">evaluateJavascript</a></li>
</ul>
<p>以下例子在H5中都定义了全局函数供Native调用</p>
<pre><code class="copyable">    function testNativeCall() &#123;
      console.log("nativeCallJs")
      return 'nativeCallJs'
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">loadUrl</h3>
<p>可以通过webView.loadUrl(“javascript: testNativeCall()”)发起调用(需要等待Js执行完成)。loadUrl的方式会刷新页面且无法获取js的回调。</p>
<h3 data-id="heading-14">evaluateJavascript</h3>
<pre><code class="copyable">webView.evaluateJavascript("javascript: testNativeCall()", new ValueCallback<String>() &#123;
    @Override
    public void onReceiveValue(String value) &#123;
        return;
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>                                 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ficantunderstand.cn%2F2021%2F07%2F07%2FJsBridge%2FevaluateJS.png" target="_blank" rel="nofollow noopener noreferrer" title="https://icantunderstand.cn/2021/07/07/JsBridge/evaluateJS.png" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcdda0e74ebf4eaba20eaf2ff116f37c~tplv-k3u1fbpfcp-zoom-1.image" alt="evaluate调用js" loading="lazy" referrerpolicy="no-referrer"></a></p>
<h2 data-id="heading-15">参考</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zoo.team%2Farticle%2Fjsbridge" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zoo.team/article/jsbridge" ref="nofollow noopener noreferrer">小白必看，JSBridge 初探</a><br>
<a href="https://juejin.cn/post/6844903840588759048" target="_blank" title="https://juejin.cn/post/6844903840588759048">跨端技能必备之JSBridge</a><br>
<a href="https://juejin.cn/post/6844903856418062350" target="_blank" title="https://juejin.cn/post/6844903856418062350">从零开始写一个 JSBridge</a></p>
<p>                            欢迎大家关注我的微信公众号-前端小板凳,一起学习</p></div>  
</div>
            