
---
title: '灵活轻巧的java接口自动化测试实战'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://www.jianshu.com/p/undefined'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://www.jianshu.com/p/undefined'
---

<div>   
<h2>前言</h2>
<p>无论是自动化测试还是自动化部署，撸码肯定少不了，所以下面的基于java语言的接口自动化测试，要想在业务上实现接口自动化，前提是要有一定的java基础。<br>
如果没有java基础，也没关系。这里小编也为大家提供了一套java基础精讲视频（虽然年代有点久2017，但是讲解内容绝对干货，小编看了很多的基础视频唯有这一套讲解到位）由于视频较大，放到了某盘上，后台回复关键字【java】即可获取。</p>
<h2>进入主题</h2>
<h6><strong>使用技术</strong></h6>
<ul>
<li>Spring Boot</li>
<li>mybatis</li>
<li>testng</li>
<li>Swagger2</li>
<li>extentreports</li>
<li>httpclient（这里抽取了一些方法非常好用）</li>
<li>log4j2</li>
</ul>
<h2>项目结构</h2>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="810" data-height="840"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-c6b77256754cbce5" data-original-width="810" data-original-height="840" data-original-format="image/png" data-original-filesize="55138" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>httpclient 抽取工具类部分方法</li>
</ul>
<pre><code>import org.apache.http.impl.client.HttpClientBuilder;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.http.client.HttpComponentsClientHttpRequestFactory;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

/**
 * @author lgl
 * @date 2020/05/15 15:19
 */
public class RestTemplateUtils &#123;
    private static final RestTemplate REST_TEMPLATE;

    static &#123;
        HttpComponentsClientHttpRequestFactory httpRequestFactory = new HttpComponentsClientHttpRequestFactory(HttpClientBuilder.create()
                .setMaxConnTotal(1000)
                .setMaxConnPerRoute(100)
                .build());
        httpRequestFactory.setConnectionRequestTimeout(5000);
        httpRequestFactory.setConnectTimeout(5000);
        httpRequestFactory.setReadTimeout(10000);
//        httpRequestFactory.setBufferRequestBody(false);
        REST_TEMPLATE = new RestTemplate(httpRequestFactory);
    &#125;

    // ----------------------------------GET-------------------------------------------------------

    /**
     * GET请求调用方式
     *
     * @param url          请求URL
     * @param responseType 返回对象类型
     * @return ResponseEntity 响应对象封装类
     */
    public static <T> ResponseEntity<T> get(String url, Class<T> responseType) &#123;
        return REST_TEMPLATE.getForEntity(url, responseType);
    &#125;

    /**
     * GET请求调用方式
     *
     * @param url          请求URL
     * @param responseType 返回对象类型
     * @param uriVariables URL中的变量，按顺序依次对应
     * @return ResponseEntity 响应对象封装类
     */
    public static <T> ResponseEntity<T> get(String url, Class<T> responseType, Object... uriVariables) &#123;
        return REST_TEMPLATE.getForEntity(url, responseType, uriVariables);
    &#125;

// ----------------------------------POST-------------------------------------------------------

    /**
     * POST请求调用方式
     *
     * @param url          请求URL
     * @param responseType 返回对象类型
     * @return
     */
    public static <T> ResponseEntity<T> post(String url, Class<T> responseType) &#123;
        return REST_TEMPLATE.postForEntity(url, HttpEntity.EMPTY, responseType);
    &#125;

    /**
     * POST请求调用方式
     *
     * @param url          请求URL
     * @param requestBody  请求参数体
     * @param responseType 返回对象类型
     * @return ResponseEntity 响应对象封装类
     */
    public static <T> ResponseEntity<T> post(String url, Object requestBody, Class<T> responseType) &#123;
        return REST_TEMPLATE.postForEntity(url, requestBody, responseType);
    &#125;

    /**
     * POST请求调用方式
     *
     * @param url          请求URL
     * @param requestBody  请求参数体
     * @param responseType 返回对象类型
     * @param uriVariables URL中的变量，按顺序依次对应
     * @return ResponseEntity 响应对象封装类
     */
    public static <T> ResponseEntity<T> post(String url, Object requestBody, Class<T> responseType, Object... uriVariables) &#123;
        return REST_TEMPLATE.postForEntity(url, requestBody, responseType, uriVariables);
    &#125;

    /**
     * POST请求调用方式
     *
     * @param url          请求URL
     * @param requestBody  请求参数体
     * @param responseType 返回对象类型
     * @param uriVariables URL中的变量，与Map中的key对应
     * @return ResponseEntity 响应对象封装类
     */
    public static <T> ResponseEntity<T> post(String url, Object requestBody, Class<T> responseType, Map<String, ?> uriVariables) &#123;
        return REST_TEMPLATE.postForEntity(url, requestBody, responseType, uriVariables);
    &#125;


</code></pre>
<h2>实战示例</h2>
<p>通过Swagger2调取controller层示例</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="380"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-a100d10f855906a4" data-original-width="1080" data-original-height="380" data-original-format="image/png" data-original-filesize="147462" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1040" data-height="461"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-986fdc3d685b0156" data-original-width="1040" data-original-height="461" data-original-format="image/png" data-original-filesize="50674" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>
<p>请求示例</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1030" data-height="618"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-3b94a52648fedf56" data-original-width="1030" data-original-height="618" data-original-format="image/png" data-original-filesize="37485" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
</li>
<li><p>响应示例</p></li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="954" data-height="868"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-0a0b947ea843aa95" data-original-width="954" data-original-height="868" data-original-format="image/png" data-original-filesize="54794" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h6>接口测试用例通过extentreports生成测试报告</h6>
<ul>
<li>执行resources下的testNG.xml生成测试用例报告<br>
示例测试报告如下：</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="528"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-ef70a51735578978" data-original-width="1080" data-original-height="528" data-original-format="image/png" data-original-filesize="202706" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><br>
<p>通过报告可以看到用例的总数，多少通过多少失败，失败的异常打印等信息。</p>

<ul>
<li>
<p>接口的并发测试<br>
测试单元ConcurrentTestCase类是测试并发的示例<br>
根据入参参数设置并发量，测试结果如下：</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="556"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-663078716189f8f5" data-original-width="1080" data-original-height="556" data-original-format="image/png" data-original-filesize="164922" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
</li>
</ul>
<p>简单的写了两个示例，具体的实现还需根据自己的接口文档去设计测试用例。<br>
项目源码传送门:<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Frootczy%2FHttpClient" target="_blank">点击获取 </a></p>
<hr>
<ul>
<li><em>更多测试技术分享、学习资源以及一些其他福利可关注公众号：【Coding测试】获取：</em></li>
</ul>
  
</div>
            