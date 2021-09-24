
---
title: 'Forest v1.5.3 正式版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7918'
author: 开源中国
comments: false
date: Fri, 24 Sep 2021 15:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7918'
---

<div>   
<div class="content">
                                                                                            <p>v1.5.3 本版发布了，本次版本更新新增了较多功能，其中有许多重大更新。</p> 
<h2>重点更新内容</h2> 
<h4>1. 新增Forest快捷接口</h4> 
<p>以前版本使用 Forest，必须先定义一个 interface 接口类，这种形式可以满足大多数情况的场景。 但若想快速访问一个url可能显得不合时宜。 所以本次更新新增了快捷接口，不用再从定义接口开始了。</p> 
<p>它大概长这个样子：</p> 
<pre><code class="language-java">
// Get请求
// 并以 String 类型接受数据
String str = Forest.get("/").executeAsString();

// Post请求
// 并以自定义的 MyResult 类型接受
MyResult myResult = Forest
   .post("/")
   .execute(MyResult.class);

// 通过 TypeRefernce 引用类传递泛型参数
// 就可以将响应数据以带复杂泛型参数的类型接受了
Result<List<User>> userList = Forest
   .post("/")
   .execute(new TypeReferenceList<Result<List<User>>>() &#123;&#125;);


// 定义各种参数
// 并以 Map 类型接受
Map<String, Object> map = Forest.post("/")
      .backend("okhttp3")        // 设置后端为 okhttp3
      .contentTypeJson()         // 设置 Content-Type 头为 application/json
      .host("127.0.0.1")         // 设置地址的host为 127.0.0.1
      .port(8080)                // 设置地址的端口为 8080
      .addBody("a", 1)           // 添加 Body 项(键值对)： a, 1
      .addBody("b", 2)           // 添加 Body 项(键值对：  b, 2
      .maxRetryCount(3)          // 设置请求最大重试次数为 3
      // 设置 onSuccess 回调函数
      .onSuccess((data, req, res) -> &#123; log.info("success!"); &#125;)
      // 设置 onError 回调函数
      .onError((ex, req, res) -> &#123; log.info("error!"); &#125;)
      // 设置请求成功判断条件回调函数
      .successWhen((req, res) -> res.noException() && res.statusOk())
      // 执行并返回Map数据类型对象
      .executeAsMap();

</code></pre> 
<h4>2. 请求成功条件/重试条件</h4> 
<p>2.1 <code>@Success</code> 注解</p> 
<p>先要定义 SuccessWhen 接口的实现类</p> 
<pre><code class="language-java">public class TestSuccessWhen implements SuccessWhen &#123;

    /**
     * 请求成功条件
     * @param req Forest请求对象
     * @param res Forest响应对象
     * @return 是否成功
     */
    @Override
    public boolean successWhen(ForestRequest req, ForestResponse res) &#123;
        // 没有异常 并且 状态码在正常范围 并且 状态码不等于203
        // 当然在这里也可以写其它条件，比如 通过 res.getData() 或 res.getConent() 获取业务数据
        // 再更具业务数据判断是否成功
        return res.noException() && res.statusOk() && res.statusCode() != 203;
    &#125;
&#125;
</code></pre> 
<p>在Forest请求接口方法上挂上 <code>@Success</code> 注解</p> 
<pre><code class="language-java">@Get("http://localhost:$&#123;port&#125;/")
@Success(condition = TestSuccessWhen.class)
String getData();
</code></pre> 
<p>若调用 getData() 后，返回的状态码为 203, 就会被认为是请求失败，如果设置了重试次数大于0，就会去执行重试任务。 若没有重试次数可用，则进入 onError 请求失败流程</p> 
<p>2.2 使用 <code>@Retry</code> 注解</p> 
<p>先定义 RetryWhen 接口实现类</p> 
<pre><code class="language-java">public class TestRetryWhen implements RetryWhen &#123;

    /**
     * 请求重试条件
     * @param request Forest请求对象
     * @param response Forest响应对象
     * @return 是否重试
     */
    @Override
    public boolean retryWhen(ForestRequest request, ForestResponse response) &#123;
        // 如果响应状态码为 203 就进行重试，尽管此时请求是成功的
        // 当然在这里也可以写其它条件，比如 通过 res.getData() 或 res.getConent() 获取业务数据
        // 再更具业务数据判断是否进行重试
        return response.statusIs(203);
    &#125;

&#125;

</code></pre> 
<p>在Forest请求接口方法上挂上 <code>@Retry</code> 注解</p> 
<pre><code class="language-java">// maxRetryCount 为最大重试次数
// maxRetryInterval 为最大重试时间间隔, 单位为毫秒
// condition 为请求重试条件，即自定义的 RetryWhen 接口实现类
@Get("http://localhost:$&#123;port&#125;/")
@Retry(maxRetryCount = "3", maxRetryInterval = "10", condition = TestRetryWhen.class)
String sendData();
</code></pre> 
<p>若调用 sendData() 后，返回的状态码为 203, 就会被认为需要重试，如果设置了重试次数大于0，就会去执行重试任务。 若没有重试次数可用，则进入 onSuccess 请求成功流程</p> 
<p>2.3 两种重试的区别</p> 
<p>可能有小伙伴有疑问，既然通过 SuccessWhen 成功条件判断失败后也可以触发重试，那为何还要 RetryWhen 呢？</p> 
<p>Forest的重试机制是这样的：1. 先判定是否成功，失败的话触发重试 2. 如果是成功的，则判断是否符合重试条件，符合的话也触发重试.</p> 
<p>这两者的区别是：</p> 
<p>因为请求失败而重试的请求，当最后一次重试也是失败的话，就会进入请求失败流程（如调用 onError）</p> 
<p>因为触发重试条件而重试的请求，此时请求判断是成功的，所以只要最后一次重试也是成功的，就会进入请求成功流程 (如调用 onSuccess)</p> 
<p>简单一句话描述： <strong>successWhen失败就重试，retryWhen即便成功也重试</strong></p> 
<p>2.4 <code>OnRetry</code> 回调函数</p> 
<p>不管是哪一种重试方式，只要触发了请求重试，都会在重试请发送之前调用 <code>OnRetry</code> 回调函数</p> 
<p>可以在拦截器中实现 onRetry 回调函数</p> 
<pre><code class="language-java">public class TestRetryInterceptor implements Interceptor<Object> &#123;

    /**
     * 在请重试前调用 onRetry 回调函数
     * 
     * @param request Forest请求对象
     * @param response Forest响应对象
     */
    @Override
    public void onRetry(ForestRequest request, ForestResponse response) &#123;
        // 将当前重试次数添加到 Forest 请求对象的附件中
        request.addAttachment("retry-interceptor", request.getCurrentRetryCount());
    &#125;
&#125;
</code></pre> 
<p>将实现了 onRetry 方法的拦截器关联到相关接口上</p> 
<pre><code class="language-java">@BaseRequest(baseURL = "http://localhost:$&#123;port&#125;/", interceptor = TestRetryInterceptor.class)
public interface RetryClient &#123;

    @Get("/")
    @Retry(maxRetryCount = "$&#123;0&#125;", maxRetryInterval = "$&#123;1&#125;", condition = TestRetryWhen.class)
    ForestRequest<String> testRetryRequest(int retryCount, long retryInterval);

    @Get("/")
    @Retry(maxRetryCount = "$&#123;0&#125;", maxRetryInterval = "$&#123;1&#125;", condition = TestRetryWhen.class)
    String testRetry(int retryCount, long retryInterval, OnSuccess<String> onSuccess);
&#125;

</code></pre> 
<p>此时 RetryClient 接口下的任意一个方法触发重试时，都会先调用 TestRetryInterceptor 拦截器类的 onRetry 方法。</p> 
<h2>其它新特性</h2> 
<h4>新增特性:</h4> 
<ul> 
 <li>feat: Forest快捷接口 (#I4893Q)</li> 
 <li>feat: 支持全局变量动态绑定方法 (#I478N2)</li> 
 <li>feat: 支持引用properties的字符串模板 (#I3P1QK)</li> 
 <li>feat: 支持获取响应原因短语，即响应状态文本 (#I4BJVF)</li> 
 <li>feat: 自定义组合注解 (#I4BISF)</li> 
 <li>feat: 可自定义请求是否成功的条件 (#I4AEMT)</li> 
 <li>feat: 可动态设置主机地址和端口号 (#I4AEJ8)</li> 
 <li>feat: 自定义重试条件 (#I493N3)</li> 
 <li>feat: 新增 OnRetry 回调函数 (#I493N6)</li> 
 <li>feat: 新增 <code>@Headers</code> 注解 (#I4BJQ6)</li> 
 <li>feat: Forest请求接口继承规则 (#I4B0N7)</li> 
 <li>feat: 自动重定向控制 (#I4B0FM)</li> 
 <li>feat: 全局变量支持动态绑定方法 (#I478N2)</li> 
 <li>feat: 在请求日志中显示后端框架名称 (#I4AKTD)</li> 
 <li>feat: 新建forest-mock子项目 (#I468JB)</li> 
</ul> 
<h4>Fix的Bug:</h4> 
<ul> 
 <li>fix: POST请求中，空Map无法转成&#123;&#125; JSON字符串 (#I455O2)</li> 
 <li>fix: 过滤器参数总是为第一个参数 (#I43VV0)</li> 
 <li>fix: 自定义请求头content-type会替换为大写 (#I46WNW)</li> 
 <li>fix: 在Spring项目中如果不配置转换器就会找不到Converter (#I46FKV)</li> 
 <li>fix: Response不带Content-Type和Content-Encoding头时无法正常解析 (#I455PO)</li> 
 <li>fix: 当请求 302 请求时，Forest 会自动的访问重定向的url，导致 302 的响应头拿不到 (#I4AF3B)</li> 
 <li>fix: SpringSSLKeyStore 在Spring中初始化失败 fix: 配置有ForestConfiguration参数的转换器的时候，在springboot中会初始化失败 (#I4AKT3)</li> 
 <li>fix: 在多线程环境下使用上传文件接口，运行时间长后会报出堆栈溢出的错误 (#I37UGY)</li> 
 <li>fix: BeanPostProcessor 接口在低版本 springboot 环境下不兼容</li> 
</ul> 
<h4>优化内容:</h4> 
<ul> 
 <li>opt: 优化 StringUtils 工具类方法</li> 
 <li>opt: 优化 URLUtils 工具类方法</li> 
</ul> 
<h4>代码改动:</h4> 
<ul> 
 <li>add: SpringForestProperties类</li> 
 <li>add: 在所有请求注解中(如 <code>@Request</code>, <code>@Get</code>)添加 responseEncoding 属性，用于强制指定响应数据的编码格式</li> 
 <li>add: SpringForestObjectFactory类 add: ForestResponse.isRedirection 方法</li> 
 <li>add: ForestResponse.getRedirectionLocation 方法</li> 
 <li>add: ForestResponse.redirectionRequest 方法</li> 
 <li>add: ForestHeaderMap.clone 方法</li> 
 <li>add: ForestQueryMap.clone 方法</li> 
 <li>refactor: retryCount属性不在建议使用</li> 
 <li>update: 去掉MethodLifeCycle</li> 
 <li>refactor: 修改Forest接口扫描逻辑</li> 
 <li>refactor: 将 TypeReference 类改为抽象类</li> 
</ul> 
<h4>特别鸣谢:</h4> 
<p>感谢他们参与的贡献，排名不分先后</p> 
<ul> 
 <li>@CHMing</li> 
 <li>@ifaxin</li> 
</ul>
                                        </div>
                                      
</div>
            