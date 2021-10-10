
---
title: 'Spring Cloud Gateway 全局通用异常处理'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/2718590-3244f977c4304d76.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/2718590-3244f977c4304d76.png'
---

<div>   
<h2>为什么需要全局异常处理</h2>
<p>在传统 Spring Boot 应用中， 我们 @ControllerAdvice 来处理全局的异常，进行统一包装返回</p>
<pre><code class="java">
// 摘至 spring cloud alibaba console 模块处理
@ControllerAdvice
public class ConsoleExceptionHandler &#123;

    @ExceptionHandler(AccessException.class)
    private ResponseEntity<String> handleAccessException(AccessException e) &#123;
        return ResponseEntity.status(HttpStatus.FORBIDDEN).body(e.getErrMsg());
    &#125;
&#125;
</code></pre>
<p>例如： ③ 处应用调用数据库异常，通过 @ControllerAdvice 包装异常请求响应给客户端</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="623" data-height="179"><img data-original-src="//upload-images.jianshu.io/upload_images/2718590-3244f977c4304d76.png" data-original-width="623" data-original-height="179" data-original-format="image/jpeg" data-original-filesize="9946" src="https://upload-images.jianshu.io/upload_images/2718590-3244f977c4304d76.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>但在微服务架构下， 例如 ② 处 网关调用业务微服务失败（转发失败、调用异常、转发失败），在应用设置的 @ControllerAdvice 将失效，因为流量根本没有转发到应用上处理。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="623" data-height="179"><img data-original-src="//upload-images.jianshu.io/upload_images/2718590-1a892d02d4cb6c71.png" data-original-width="623" data-original-height="179" data-original-format="image/jpeg" data-original-filesize="9956" src="https://upload-images.jianshu.io/upload_images/2718590-1a892d02d4cb6c71.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>如上图： 模拟所有路由断言都不匹配 404 , 和 spring boot 默认保持一致的错误输出页面。 显然我们在网关同样配置 @ControllerAdvice 是不能解决问题,因为 spring cloud gateway 是基于 webflux 反应式编程。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1035" data-height="208"><img data-original-src="//upload-images.jianshu.io/upload_images/2718590-43ad08b6d8cc6519.png" data-original-width="1035" data-original-height="208" data-original-format="image/jpeg" data-original-filesize="27490" src="https://upload-images.jianshu.io/upload_images/2718590-43ad08b6d8cc6519.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h2>解决方法</h2>
<h3>默认处理流程</h3>
<ul>
<li>ExceptionHandlingWebHandler 作为 spring cloud gateway 最核心 WebHandler 的一部分会进行异常处理的过滤</li>
</ul>
<pre><code class="java">public class ExceptionHandlingWebHandler extends WebHandlerDecorator &#123;
    @Override
    public Mono<Void> handle(ServerWebExchange exchange) &#123;
        Mono<Void> completion;
        try &#123;
            completion = super.handle(exchange);
        &#125;
        catch (Throwable ex) &#123;
            completion = Mono.error(ex);
        &#125;

     // 获取全局的 WebExceptionHandler 执行
        for (WebExceptionHandler handler : this.exceptionHandlers) &#123;
            completion = completion.onErrorResume(ex -> handler.handle(exchange, ex));
        &#125;
        return completion;
    &#125;
&#125;
</code></pre>
<ul>
<li>默认实现 DefaultErrorWebExceptionHandler</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1920" data-height="213"><img data-original-src="//upload-images.jianshu.io/upload_images/2718590-b2b50c0c9b854a58.png" data-original-width="1920" data-original-height="213" data-original-format="image/jpeg" data-original-filesize="69909" src="https://upload-images.jianshu.io/upload_images/2718590-b2b50c0c9b854a58.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<pre><code class="java">public class DefaultErrorWebExceptionHandler  &#123;

    @Override
    protected RouterFunction<ServerResponse> getRoutingFunction(ErrorAttributes errorAttributes) &#123;
     // 根据客户端 `accpet` 请求头决定返回什么资源，如上浏览器返回的是 页面
        return route(acceptsTextHtml(), this::renderErrorView).andRoute(all(), this::renderErrorResponse);
    &#125;
&#125;
</code></pre>
<pre><code class="shell">
// 模拟指定 `accpet` 情况
curl --location --request GET 'http://localhost:9999/adminx/xx' \  18:09:23
     --header 'Accept: application/json'
&#123;"timestamp":"2020-05-24 18:09:24","path":"/adminx/xx","status":404,"error":"Not Found","message":null,"requestId":"083c48e3-2"&#125;⏎
</code></pre>
<h3>重写 ErrorWebExceptionHandler</h3>
<pre><code class="java">/**
 * @author lengleng
 * @date 2020/5/23
 * <p>
 * 网关异常通用处理器，只作用在webflux 环境下 , 优先级低于 &#123;@link ResponseStatusExceptionHandler&#125; 执行
 */
@Slf4j
@Order(-1)
@RequiredArgsConstructor
public class GlobalExceptionConfiguration implements ErrorWebExceptionHandler &#123;
    private final ObjectMapper objectMapper;

    @Override
    public Mono<Void> handle(ServerWebExchange exchange, Throwable ex) &#123;
        ServerHttpResponse response = exchange.getResponse();

        if (response.isCommitted()) &#123;
            return Mono.error(ex);
        &#125;

        // header set
        response.getHeaders().setContentType(MediaType.APPLICATION_JSON);
        if (ex instanceof ResponseStatusException) &#123;
            response.setStatusCode(((ResponseStatusException) ex).getStatus());
        &#125;

        return response
                .writeWith(Mono.fromSupplier(() -> &#123;
                    DataBufferFactory bufferFactory = response.bufferFactory();
                    try &#123;
                        return bufferFactory.wrap(objectMapper.writeValueAsBytes(R.failed(ex.getMessage())));
                    &#125; catch (JsonProcessingException e) &#123;
                        log.warn("Error writing response", ex);
                        return bufferFactory.wrap(new byte[0]);
                    &#125;
                &#125;));
    &#125;
&#125;
</code></pre>
<h2>总结</h2>
<ul>
<li>重写的 DefaultErrorWebExceptionHandler 优先级一定要小于内置 ResponseStatusExceptionHandler 经过它处理的获取对应错误类的 响应码</li>
<li>其他扩展 可以参考 SentinelBlockExceptionHandler sentinel 整合网关的处理，不过整体和默认的异常处理没有什么区别</li>
<li>基础环境说明：Spring Cloud Hoxton.SR4 & Spring Boot 2.3.0</li>
<li>具体实现代码参考：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgitee.com%2Flog4j%2Fpig" target="_blank">https://gitee.com/log4j/pig</a><br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2182" data-height="324"><img data-original-src="//upload-images.jianshu.io/upload_images/2718590-2a1452b3b99faf97.png" data-original-width="2182" data-original-height="324" data-original-format="image/png" data-original-filesize="16708" src="https://upload-images.jianshu.io/upload_images/2718590-2a1452b3b99faf97.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
</li>
</ul>
  
</div>
            