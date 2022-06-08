
---
title: 'springCloud --- 高级篇(2)'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/11531502-d6bbe6775f28b74a.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/11531502-d6bbe6775f28b74a.png'
---

<div>   
<p>本系列笔记涉及到的代码在GitHub上，地址：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fzsllsz%2Fcloud" target="_blank">https://github.com/zsllsz/cloud</a></p>
<p>本文涉及知识点：</p>
<ul>
<li><p>sentinel降级；</p></li>
<li><p>sentinel熔断；</p></li>
<li><p>sentinel规则持久化；</p></li>
</ul>
<hr>
<p>欢迎大家关注我的公众号 <strong>javawebkf</strong>，目前正在慢慢地将简书文章搬到公众号，以后简书和公众号文章将同步更新，且简书上的付费文章在公众号上将免费。</p>
<hr>
<h1>一、springCloud Alibaba sentinel 之降级规则</h1>
<p>上一篇已经说了sentinel的流控，接下来看看sentinel的降级。<br>
<strong>1、基本介绍：</strong><br>
sentinel的降级没有半开状态，有如下3种策略：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="840" data-height="375"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-d6bbe6775f28b74a.png" data-original-width="840" data-original-height="375" data-original-format="image/png" data-original-filesize="28888" src="https://upload-images.jianshu.io/upload_images/11531502-d6bbe6775f28b74a.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">sentinel降级</div>
</div>
<ul>
<li><p>RT(平均响应时间)：平均响应时间超出阈值且在时间窗口期内通过的大于等于5，两个条件同时满足后触发降级。窗口期过后关闭断路器。注意 Sentinel 默认统计的 RT 上限是 4900 ms，超出此阈值的都会算作 4900 ms，若需要变更此上限可以通过启动配置项 -Dcsp.sentinel.statistic.max.rt=xxx 来配置。</p></li>
<li><p>异常比例(秒级)：QPS大于等于5且异常比例超过阈值时，触发降级。时间窗口结束后，关闭降级。</p></li>
<li><p>异常数(分钟级)：异常数超过阈值时触发降级，时间窗口结束后关闭降级。</p></li>
</ul>
<p><strong>2、RT策略实例：</strong></p>
<ul>
<li>在8401的controller中加上一个方法，如下：</li>
</ul>
<pre><code>@GetMapping("/testC")
public String testC() &#123;
    try &#123;
        TimeUnit.SECONDS.sleep(1);
    &#125; catch (InterruptedException e) &#123;
        e.printStackTrace();
    &#125;
    return "=========== test RT ==========";
&#125;
</code></pre>
<ul>
<li>sentinel降级配置：</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="843" data-height="372"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-09f470632d65f5ed.png" data-original-width="843" data-original-height="372" data-original-format="image/png" data-original-filesize="29746" src="https://upload-images.jianshu.io/upload_images/11531502-09f470632d65f5ed.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">sentinel RT降级配置</div>
</div>
<p>这里配置的意思就是，1秒钟内有超过5个请求进入时，要求每个请求testC在200毫秒内响应，如果没有响应，那就跳闸1秒中，接下来的1秒内的请求都会被降级，1秒后恢复。用jmeter请求testC，用10个线程去请求，每1秒请求1次。然后再在浏览器请求testC，就会发现访问不了，返回<code>Blocked by Sentinel (flow limiting)</code>。</p>
<p><strong>3、异常比例策略实例：</strong></p>
<ul>
<li>在8401的controller中加上一个方法，如下：</li>
</ul>
<pre><code>@GetMapping("/testD")
public String testD() &#123;
    int x = 10 / 0;
    return "============ test 异常比例 ============";
&#125;
</code></pre>
<ul>
<li>sentinel降级配置：</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="832" data-height="368"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-22a427e430c3bf32.png" data-original-width="832" data-original-height="368" data-original-format="image/png" data-original-filesize="30528" src="https://upload-images.jianshu.io/upload_images/11531502-22a427e430c3bf32.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">sentinel异常比例降级配置</div>
</div>
<p>这个配置意思就是，1秒中内超过5个请求的时候，如果有超过<code>5*0.2=1</code>个请求异常了，那么在接下来的2秒内都会拉闸断电。降级后访问结果如下：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="706" data-height="273"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-1aab0dd9f1ff8309.png" data-original-width="706" data-original-height="273" data-original-format="image/png" data-original-filesize="10838" src="https://upload-images.jianshu.io/upload_images/11531502-1aab0dd9f1ff8309.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">sentinel异常比例降级</div>
</div>
<p><strong>4、异常数策略实例：</strong><br>
最近1分钟内请求发生异常的数量超过阈值时会触发降级。由于这里的异常数是分钟级别统计的，所以如果时间窗口期设置的小于60秒，则结束熔断后可能再次进入熔断状态。所以，时间窗口期要大于等于60秒。</p>
<ul>
<li>仍旧用testD进行测试</li>
<li>sentinel降级配置：</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="838" data-height="361"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-d1c6cd4ff8822a1f.png" data-original-width="838" data-original-height="361" data-original-format="image/png" data-original-filesize="28450" src="https://upload-images.jianshu.io/upload_images/11531502-d1c6cd4ff8822a1f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">sentinel异常数降级配置</div>
</div>
<p>这个配置表示，1分钟内对testD的请求发生异常的次数超过3次，那么接下来的66秒内都会拉闸断电。我们在1分钟内访问3次，然后再去访问，就会返回<code>Blocked by Sentinel (flow limiting)</code>。</p>
<h1>二、springCloud Alibaba sentinel 之热点规则</h1>
<p><strong>1、是什么？</strong><br>
就是针对热点数据做限流。比如id为1的商品是热点数据，那么可以针对id为1的这个商品做限流。</p>
<p><strong>2、热点限流实例配置：</strong></p>
<ul>
<li>在8401的controller中加一个方法，如下：</li>
</ul>
<pre><code>@GetMapping("/testHotKey")
@SentinelResource(value = "testHotKey", blockHandler = "deal_testHotKey") // 这个value值随意，只要唯一即可，但是一般和@GetMapping中的一致
public String testHotKey(@RequestParam(value = "p1", required = false) String p1,
                         @RequestParam(value = "p2", required = false) String p2) &#123;
        return "test hot key";
&#125;

/**
* 兜底方法，参数除了原方法的参数，还要加上BlockException
* @param p1
* @param p2
* @param e
* @return
*/
public String deal_testHotKey(String p1, String p2, BlockException e) &#123;
    return "兜底方法";
&#125;
</code></pre>
<ul>
<li>热点规则配置：</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="833" data-height="512"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-2d73e78933968934.png" data-original-width="833" data-original-height="512" data-original-format="image/png" data-original-filesize="37611" src="https://upload-images.jianshu.io/upload_images/11531502-2d73e78933968934.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">热点规则配置</div>
</div>
<p>这里配置的意思就是，testHotKey（就是@SentinelResource中的value值）这个资源，我对索引为0的参数(p1)进行监控，如果访问testHotKey带上了p1，并且QPS超过了1，那么接下来的1秒中内这个方法都会被降级。注意：索引为0的参数是p1，是controller中接收参数的顺序的索引。你访问<code>http://192.168.0.104:8401/sentinel/testHotKey?p2=1</code>，这里只有一个参数p2，在url中它是第0个参数，但是在controller中不是，所以这样访问并不会被降级。</p>
<p><strong><em>热点配置的高级选项：</em></strong></p>
<ul>
<li>参数例外项：上面的配置对p1进行限流，不管p1的值是多少，只要QPS超过1，就降级。现在的需求是如果p1的值是5，我就搞特殊的，因为它充了钱，所以让它QPS超过100才限流。配置如下图：</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="841" data-height="813"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-f733a54291a91964.png" data-original-width="841" data-original-height="813" data-original-format="image/png" data-original-filesize="66287" src="https://upload-images.jianshu.io/upload_images/11531502-f733a54291a91964.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">参数例外项配置</div>
</div>
<p>当参数不是5时，QPS超过1就会被限流降级，p1的值为5时，你狂点都可以正常访问。<br>
<strong>注意：</strong>@SentinelResource只管我们控制台配置的违规情况，才会进行兜底，假如程序异常了，它是管不了的。比如我们在return 前加一行<code>int a = 10 / 0</code>，它还是会返回error page的，而不是兜底方法。</p>
<h1>三、springCloud Alibaba sentinel 之系统规则</h1>
<p>上面的限流降级都是针对某个具体方法而言的，系统规则就是针对整个微服务系统来说的。比如配置了QPS阈值为100，也就是说，这个微服务的QPS超过100，整个服务都不可用了。就是控制的粒度更粗了，生产中不建议用这种方式。</p>
<p><strong>1、系统规则的阈值类型：</strong></p>
<ul>
<li>LOAD(对Linux和Unix机器生效)：当系统装载数超过阈值就会限流，阈值一般设置为<code>cpu核心数 * 2.5</code>
</li>
<li>RT(平均响应时间)：单台机器上所有入口流量平均RT超过阈值时进行限流降级</li>
<li>线程数：单台机器上的所有入口流量的并发线程数超过阈值时进行限流降级</li>
<li>入口QPS：当单台机器所有入口流量的QPS超过阈值时进行限流降级</li>
<li>CPU使用率：当系统cpu使用率超过阈值时进行限流降级</li>
</ul>
<p><strong>2、配置全局QPS：</strong></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="839" data-height="320"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-bf8888e32ce85678.png" data-original-width="839" data-original-height="320" data-original-format="image/png" data-original-filesize="23794" src="https://upload-images.jianshu.io/upload_images/11531502-bf8888e32ce85678.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">入口QPS</div>
</div>
<p>之前testB是没配置任何限流规则的，1秒点n次都可以，现在配了系统规则后，发现testB也是只能1秒钟点1次了，说明配置生效。</p>
<h1>四、sentinel的@SentinelResource详细用法</h1>
<p>上面做限流时用到过这个注解，但是没说其用法，下面来学习一下它的用法。<br>
<strong>1、按资源名称限流 + 后续处理：</strong></p>
<ul>
<li>修改8401的pom，添加自己定义的common模块，如下：</li>
</ul>
<pre><code><dependency>
    <groupId>com.zhu.springcloud</groupId>
    <artifactId>cloud-api-commons</artifactId>
    <version>$&#123;project.version&#125;</version>
</dependency>
</code></pre>
<ul>
<li>8401中新加一个controller，如下：</li>
</ul>
<pre><code>@RestController
@RequestMapping("/ratelimit")
public class RateLimitController &#123;

    @GetMapping("/bySource")
    @SentinelResource(value = "bySource", blockHandler = "handleException")
    public JsonResult<?> bySource() &#123;
        return new JsonResult<Payment>(200, "按资源名称限流测试通过", new Payment(1L, "6666"));
    &#125;
    
    public JsonResult<?> handleException(BlockException e)&#123;
        return new JsonResult<>(400, e.getClass().getCanonicalName() + "\t服务不可用");
    &#125;
&#125;
</code></pre>
<ul>
<li>然后新增流控规则，阈值类型选择QPS，阈值设置为1。然后访问bySource，点击快一点，就返回如下内容：</li>
</ul>
<pre><code>&#123;
  code: 400,
  message: "com.alibaba.csp.sentinel.slots.block.flow.FlowException 服务不可用",
  data: null
&#125;
</code></pre>
<ul>
<li>现在关闭8401，然后刷新sentinel dashboard，发现刚才添加的流控规则没了。所以后续得做持久化处理。</li>
</ul>
<p><strong>2、按url进行限流：</strong><br>
什么叫按资源名称，什么叫按url？看下图：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="792" data-height="391"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-5b62a2a7df4a20d7.png" data-original-width="792" data-original-height="391" data-original-format="image/png" data-original-filesize="34427" src="https://upload-images.jianshu.io/upload_images/11531502-5b62a2a7df4a20d7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">簇点链路</div>
</div>
<p>第一个<code>/ratelimit/bySource</code>就是url，第二个<code>bySource</code>就是资源名称。上面演示了按资源名称来限流，下面演示按url来限流。</p>
<ul>
<li>在RateLimitController 中添加如下方法：</li>
</ul>
<pre><code>@GetMapping("/byUrl")
@SentinelResource(value = "byUrl")
public JsonResult<?> byUrl()&#123;
    return new JsonResult<Payment>(200, "按url限流测试通过", new Payment(1L, "6666"));
&#125;
</code></pre>
<ul>
<li>配置的时候，选择url，添加流控，阈值类型QPS，阈值1。QPS超过1就会返回错误提示<code>Blocked by Sentinel (flow limiting)</code>。</li>
</ul>
<p><strong><em>这两个配置案例主要是两个知识点：</em></strong></p>
<ul>
<li>可以按url配，也可以按资源名成配</li>
<li>自己写了blockHandler就会走自己写的，没写就返回默认提示</li>
</ul>
<p><strong><em>上面的配置案例存在的问题：</em></strong></p>
<ul>
<li>兜底方案与业务代码耦合</li>
<li>每个方法都要写一个兜底方法，即没有做全局的兜底方法</li>
<li>服务一关闭，配置就没有了，即没有做持久化</li>
</ul>
<p>下面就来解决这些问题。</p>
<p><strong>3、自定义限流处理逻辑：</strong><br>
这是为了解决上面的第一第二个问题的。</p>
<ul>
<li>自定义限流处理类：</li>
</ul>
<pre><code>public class CustomerBlockHandler &#123;
    
    public static JsonResult<?> handlerException1(BlockException e)&#123;
        return new JsonResult<Payment>(444, "自定义返回信息1");
    &#125;
    
    public static JsonResult<?> handlerException2(BlockException e)&#123;
        return new JsonResult<Payment>(444, "自定义返回信息2");
    &#125;
&#125;
</code></pre>
<ul>
<li>RateLimitController:</li>
</ul>
<pre><code>@GetMapping("/customerBlockHandler")
@SentinelResource(value = "customerBlockHandler", blockHandlerClass = CustomerBlockHandler.class, blockHandler = "handlerException1")
public JsonResult<?> customerBlockHandler()&#123;
    return new JsonResult<Payment>(200, "自定义限流处理测试通过", new Payment(1L, "6666"));
&#125;
</code></pre>
<ul>
<li>sentinel控制台配置：也是配置QPS、1就好了</li>
<li>测试：1秒点击两次，发现返回：</li>
</ul>
<pre><code>&#123;
  code: 444,
  message: "自定义返回信息1",
  data: null
&#125;
</code></pre>
<p>说明自定义返回信息成功了。</p>
<h1>五、sentinel的熔断功能</h1>
<p><strong>1、Ribbon系类：</strong></p>
<p><strong><em>新建名为cloudalibaba-provider-payment9003和cloudalibaba-provider-payment9004的module，两个module只是端口不一致：</em></strong></p>
<ul>
<li>pom.xml：</li>
</ul>
<pre><code><dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator </artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
    <scope>runtime</scope>
    <optional>true</optional>
</dependency>
<!-- nacos -->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
</dependency>
<dependency>
    <groupId>com.zhu.springcloud</groupId>
    <artifactId>cloud-api-commons</artifactId>
    <version>$&#123;project.version&#125;</version>
</dependency>
<!-- sentinel -->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
</dependency>
</code></pre>
<ul>
<li>application.yml：</li>
</ul>
<pre><code>server:
  port: 9003
  
spring:
  application:
    name: nacos-payment-provider
  cloud:
    nacos:
      discovery:
        server-addr: 192.168.0.106:8848
management:
  endpoints:
    web:
      exposure:
        include:
        - "*"
</code></pre>
<ul>
<li>主启动类：</li>
</ul>
<pre><code>@SpringBootApplication
@EnableDiscoveryClient
public class PaymentMain9003 &#123;
    public static void main(String[] args) throws Exception &#123;
        SpringApplication.run(PaymentMain9003.class, args);
    &#125;
&#125;
</code></pre>
<ul>
<li>业务类：</li>
</ul>
<pre><code>@RestController
@RequestMapping("/payment")
public class PaymentController &#123;
    
    @Value("$&#123;server.port&#125;")
    private int port;
    
    public static Map<Long, Payment> map = new HashMap<>();
    // 偷懒，不去连数据库查记录了
    static &#123;
        map.put(1L, new Payment(1L,"111"));
        map.put(1L, new Payment(2L,"222"));
        map.put(1L, new Payment(3L,"333"));
    &#125;
    
    @GetMapping("/&#123;id&#125;")
    public JsonResult<?> payment(@PathVariable("id") Long id)&#123;
        return new JsonResult<>(200, "success from " + port, map.get(id));
    &#125;
&#125;
</code></pre>
<p><strong><em>新建名为cloudalibaba-consumer-nacos-order84的消费者，通过ribbon去调用9003和9004:</em></strong></p>
<ul>
<li>pom.xml：</li>
</ul>
<pre><code><dependency>
    <groupId>com.zhu.springcloud</groupId>
    <artifactId>cloud-api-commons</artifactId>
    <version>$&#123;project.version&#125;</version>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator </artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
    <scope>runtime</scope>
    <optional>true</optional>
</dependency>
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>
<!-- nacos -->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
</dependency>
<!-- sentinel -->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
</dependency>
</code></pre>
<ul>
<li>application.yml：</li>
</ul>
<pre><code>server:
  port: 84
spring:
  application:
    name: nacos-order-consumer
  cloud:
    nacos:
      discovery:
        server-addr: 192.168.0.106:8848
    sentinel:
      transport:
        client-ip: 192.168.0.104
        dashboard: 192.168.0.106:8080
        port: 8719
service-url:
  nacos-user-service: http://nacos-payment-provider
</code></pre>
<ul>
<li>主启动类：</li>
</ul>
<pre><code>@SpringBootApplication
@EnableDiscoveryClient
public class OrderMain84 &#123;
    public static void main(String[] args) throws Exception &#123;
        SpringApplication.run(OrderMain84.class, args);
    &#125;
&#125;
</code></pre>
<ul>
<li>ribbon配置类：</li>
</ul>
<pre><code>@Configuration
public class RibbonConfig &#123;
    @Bean
    @LoadBalanced
    public RestTemplate getRestTemplate() &#123;
        return new RestTemplate();
    &#125;
&#125;
</code></pre>
<ul>
<li>controller：</li>
</ul>
<pre><code>@RestController
@RequestMapping("/order")
public class OrderController &#123;

    @Value("$&#123;service-url.nacos-user-service&#125;")
    private String url;
    
    @Autowired
    private RestTemplate restTemplate;
    
    @GetMapping("/fallback/&#123;id&#125;")
    @SentinelResource(value = "fallback")
    public JsonResult<?> fallback(@PathVariable("id") Long id)&#123;
        JsonResult<?> result = restTemplate.getForObject(url + "/payment/" + id, JsonResult.class);
        if (id == 4) &#123;
            throw new IllegalArgumentException("非法参数");
        &#125; else if (result.getData() == null) &#123;
            throw new NullPointerException("没有该id对应的记录");
        &#125;
        return result;
    &#125;
&#125;
</code></pre>
<p><strong><em>现在访问<code>http://192.168.0.104:84/order/fallback/1</code>，可以成功返回信息，并且一次9003一次9004。如果传的id是4，就会返回error page，非法参数，因为我们没有任何配置。要解决这个问题，可以在@SentinelResource中加上fallback属性，属性值就是发生异常时要调用的方法名，如下：</em></strong></p>
<pre><code>public JsonResult<?> handlerFallback(@PathVariable("id") Long id, Throwable e)&#123;
    return new JsonResult<>(444, "没有id" + id + "对应的记录，这是兜底方法，" + e.getMessage());
&#125;
</code></pre>
<p>这样，再去访问<code>http://192.168.0.104:84/order/fallback/4</code>，返回的信息就如下：</p>
<pre><code>&#123;
  code: 444,
  message: "没有id4对应的记录，这是兜底方法，非法参数",
  data: null
&#125;
</code></pre>
<p><strong><em>这里说一下fallback和blockHandler的区别：</em></strong></p>
<ul>
<li>fallback：管运行异常，运行时发生异常了，就走fallback</li>
<li>blockHandler：sentinel控制台的配置违规处理，就是前面讲的那些降级规则，违规了就走blockHandler</li>
</ul>
<p><strong><em>下面就看一下两个都配置的情况：</em></strong></p>
<pre><code>    @GetMapping("/fallback/&#123;id&#125;")
    @SentinelResource(value = "fallback", fallback = "handlerFallback", blockHandler = "blockHandler")
    public JsonResult<?> fallback(@PathVariable("id") Long id)&#123;
        JsonResult<?> result = restTemplate.getForObject(url + "/payment/" + id, JsonResult.class);
        if (id == 4) &#123;
            throw new IllegalArgumentException("非法参数");
        &#125; else if (result.getData() == null) &#123;
            throw new NullPointerException("没有该id对应的记录");
        &#125;
        return result;
    &#125;
    
    
    public JsonResult<?> handlerFallback(@PathVariable("id") Long id, Throwable e)&#123;
        return new JsonResult<>(444, "没有id" + id + "对应的记录，这是兜底方法，" + e.getMessage());
    &#125;
    
    
    public JsonResult<?> blockHandler(@PathVariable("id") Long id, BlockException e)&#123;
        return new JsonResult<>(445, "id" + id + "的记录配置违规了，这是兜底方法，" + e.getMessage());
    &#125;
</code></pre>
<p>然后在sentinel控制台配置一条流控规则，QPS阈值为1。现在访问<code>http://192.168.0.104:84/order/fallback/4</code>，如果慢悠悠地点，返回的是fallback的内容，如果快快地点，QPS大于1，返回的就是blockHandler的内容。</p>
<p><strong><em>异常忽略属性：</em></strong><code>exceptionsToIgnore = &#123;XxxException.class&#125;</code>：@SentinelResource注解还有这个属性可以配置，表示运行时发生了XxxException就忽略掉，不会走兜底的方法。</p>
<p><strong>2、openFeign系列：</strong><br>
上面的order84是通过ribbon去调用9003和9004的，这里再来演示一下通过openFeign调用服务端的时候，如果用sentinel做熔断降级相关配置。新建一个名为<strong><em>cloudalibaba-consumer-nacos-order85</em></strong>的module：</p>
<ul>
<li>pom.xml：相比order84，只多了一个openfeign：</li>
</ul>
<pre><code><!-- openfeign -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
</code></pre>
<ul>
<li>application.yml：相比order84，就是增加了sentinel激活openfeign的配置</li>
</ul>
<pre><code>server:
  port: 85
spring:
  application:
    name: nacos-order-consumer
  cloud:
    nacos:
      discovery:
        server-addr: 192.168.0.106:8848
    sentinel:
      transport:
        client-ip: 192.168.0.104
        dashboard: 192.168.0.106:8080
        port: 8719
service-url:
  nacos-user-service: http://nacos-payment-provider
  
# 激活sentinel对openfeign的支持
feign:
  sentinel:
    enabled: true
</code></pre>
<ul>
<li>主启动类：</li>
</ul>
<pre><code>@SpringBootApplication
@EnableDiscoveryClient
@EnableFeignClients // 激活openfeign
public class OrderMain85 &#123;
    public static void main(String[] args) throws Exception &#123;
        SpringApplication.run(OrderMain85.class, args);
    &#125;
&#125;
</code></pre>
<ul>
<li>service：</li>
</ul>
<pre><code>@FeignClient(value = "nacos-payment-provider", fallback = OrderServiceImpl.class)
public interface OrderService &#123;

    @GetMapping("/payment/&#123;id&#125;")
    public JsonResult<?> payment(@PathVariable("id") Long id);
&#125;
</code></pre>
<ul>
<li>serviceImpl：</li>
</ul>
<pre><code>@Component
public class OrderServiceImpl implements OrderService&#123;

    @Override
    public JsonResult<?> payment(Long id) &#123;
        return new JsonResult<>(446, "这是兜底的方法");
    &#125;
&#125;
</code></pre>
<ul>
<li>controller：</li>
</ul>
<pre><code>@RestController
@RequestMapping("/order")
public class OrderController &#123;
    
    @Autowired
    private OrderService orderService;
    
    @GetMapping("/fallback/&#123;id&#125;")
    public JsonResult<?> fallback(@PathVariable("id") Long id)&#123;
        return orderService.payment(id);
    &#125;
&#125;
</code></pre>
<p>现在访问<code>http://192.168.0.104:85/order/fallback/1</code>可以成功调用9003和9004，现在把9003和9004服务停掉，再次访问，就返回了：</p>
<pre><code>&#123;
  code: 446,
  message: "这是兜底的方法",
  data: null
&#125;
</code></pre>
<p>说明降级配置成功。</p>
<p><strong>3、熔断框架比较：</strong></p>
<h1>六、sentinel规则持久化</h1>
<p>目前我们没有做sentinel规则持久化，也就是说，在sentinel控制台配置的规则，只要我们微服务一重启，配置的规则就消失了。</p>
<p><strong>1、sentinel规则持久化的方案：</strong><br>
将规则配置进nacos进行保存，nacos也做了数据库的持久化，所以相当于间接地把sentinel规则也写进了数据库。</p>
<p><strong>2、步骤：</strong><br>
以8401的那个项目为例，进行如下修改：</p>
<ul>
<li>pom.xml：添加如下依赖：</li>
</ul>
<pre><code><dependency>
    <groupId>com.alibaba.csp</groupId>
    <artifactId>sentinel-datasource-nacos</artifactId>
</dependency>
</code></pre>
<ul>
<li>application.yml：添加nacos数据源配置</li>
</ul>
<pre><code>server:
  port: 8401
spring:
  application:
    name: cloudalibaba-sentinel-service
  cloud:
    nacos:
      discovery:
        server-addr: 192.168.0.106:8848
    sentinel:
      transport: 
        dashboard: 192.168.0.106:8080
        client-ip: 192.168.0.104
        port: 8719 # 默认8719，如果被占用会依次加1，直至找到没有被占用的端口
      datasource: # 将规则配置进nacos
        dsl: 
          nacos:
            server-addr: 192.168.0.106:8848
            data-id: cloudalibaba-sentinel-service
            group-id: DEFAULT_GROUP
            rule-type: flow
            data-type: json
# actuator图形化配置
management:
  endpoints:
    web:
      exposure:
        include:
        - "*"
</code></pre>
<ul>
<li>然后在nacos中新建配置：Data ID就是8401的服务名称，group用默认的，配置格式选json，配置内容如下：</li>
</ul>
<pre><code>[
    &#123;
        "resource":"/ratelimit/byUrl",
        "limitApp":"default",
        "grade":1,
        "count":1,
        "strategy":0,
        "controlBehavior":0,
        "clusterMode":true
    &#125;
]
</code></pre>
<p>现在说明一下json中各个字段的意思：</p>
<ul>
<li>resource：资源名称</li>
<li>limitApp：来源应用</li>
<li>grade：阈值类型，0表示线程数，1表示QPS</li>
<li>count：单机阈值</li>
<li>strategy：流控模式，0表示直接，1表示关联，2表示链路</li>
<li>controlBehavior：流控效果，0表示快速失败，1表示warm up，2表示排队等待</li>
<li>clusterMode：是否集群</li>
</ul>
<p>然后重启8401，访问一下/ratelimit/byUrl，然后发现sentinel流控中就有相关规则了，然后关闭8401，再重启，发现规则还在，并不用重新配置。关于sentinel的持久化还有很多方式，以后再细说。</p>
  
</div>
            