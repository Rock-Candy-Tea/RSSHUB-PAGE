
---
title: '参数校验神器 hibernate-validator 配合统一异常处理'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f5696092b974bc5a0745bc7b61c9f8a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 22:21:35 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f5696092b974bc5a0745bc7b61c9f8a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">传统的参数校验</h2>
<p>我相信大家在开发过程中都很头疼对前端传过来的参数进行校验，因为有时候接口需要的参数很多，在远古时代我们的校验方式应该是这样的：</p>
<pre><code class="copyable">    @PostMapping("/order/submit")
    public void submit(@RequestBody OrderRequest order)&#123;
        if(order.getParam1() == null)&#123;
            throw new XXXException("xxx不能为空");
        &#125; else if(order.getParam2() == null)&#123;
            throw new XXXException("xxx不能为空");
        &#125;
        ...
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好家伙，如果一个接口几十个参数我觉得能把人写奔溃啊……如果说不对请求参数进行校验的话，那问题更严重，在和前端联调的时候可能出现各种参数不匹配、不合法问题，这样的话我觉得前后端都会崩溃。。。。也许你会说，不是有 swagger 这种文档吗？带 "*" 就表示必传啊。但是你要知道，这个只是告诉前端这个是必传的，并不能实际限制接口，如果前端就是忘了传呢？所以后台做参数校验是必要的</p>
<h2 data-id="heading-1">尝试优化解决</h2>
<p>聪明的小伙伴可能已经想到了，根本没必要每个接口都写这些判断嘛，我自己定义一个注解，在拦截器里面拦截这些请求，判断请求对象的字段上有没有加我定义的注解就行了，假设我们自己定义一个注解</p>
<pre><code class="copyable">/**
 * 自定义注解
 * */
@Documented
@Target( &#123;ElementType.FIELD&#125;)
@Retention(RetentionPolicy.RUNTIME)
public @interface NotNull &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在请求参数实体类中使用我们定义的注解</p>
<pre><code class="copyable">@Data
public class OrderRequest &#123;
    //自己定义的注解
    @NotNull
    private String merchantCode;
    
    @NotNull
    private String memberCode;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拦截器中做统一校验</p>
<pre><code class="copyable">    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception &#123;
        HandlerMethod handlerMethod = (HandlerMethod)handler;
        //先获取参数列表
        Parameter[] parameters = handlerMethod.getMethod().getParameters();
        for (Parameter parameter : parameters) &#123;
            //获取参数字段
            Field[] declaredFields = parameter.getType().getDeclaredFields();
            for (Field declaredField : declaredFields) &#123;
                NotNull annotation = declaredField.getAnnotation(NotNull.class);
                //如果该字段有NotNull注解
                if(annotation != null)&#123;
                    declaredField.setAccessible(true);
                    String s = declaredField.get(getTargetObject(parameter,request)).toString();//实际值
                    if(s == null)&#123;
                        //这里应该组装信息返回给前端，为了简单就直接 throw
                        throw new RuntimeException(declaredField.getName()+"：不能为NULL");
                    &#125;
                &#125;
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样一个简单地 NotNull 校验就完成了，看似简单，不过 getTargetObject 方法我并没有去实现，这里要拿到目标对象（也就是上面 controller 方法的 order 对象）还是比较麻烦的，因为我们在这里只能通过反射拿到类型、字段等信息。如果要拿到目标对象，还得从 HttpServletRequest 这里拿到字节流去做转换，也就是 SpringMVC 的参数解析和数据绑定那里做的工作。</p>
<h2 data-id="heading-2">强大的 hibernate-validator</h2>
<p>你可能已经发现了，我们刚刚实现的自定义校验非常简陋，只做了一个不为空的校验，而且我们实现的是在拦截器里面，走到拦截器时，数据绑定这些其实已经结束了。对此，有一个框架 hibernate-validator 帮我们解决了这个问题。</p>
<p>在谈它之前我们需要了解一下 JSR（Java Specification Requests）规范，JSR 303 是 Java 官方提出的数据校验规范 叫做 Bean Validation，现在已经到了 2.0 版本，对应 JSR 380 。就像 Servlet 一样，只提了一个规范，具体的由我们实现。 hibernate-validator 就遵循这个规范做出了一套实现。</p>
<p>本篇文章以 SpringBoot 为例，在 SpringBoot 中使用非常方便，直接引入 starter 即可， SpringBoot 会帮我们自动配置</p>
<pre><code class="copyable">        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入之后就可以使用它提供的一系列校验注解，现在我们将自定义注解换成框架提供的注解，删掉之前的拦截器</p>
<pre><code class="copyable">@Data
public class OrderRequest &#123;
    //hibernate-validator 提供的注解
    @javax.validation.constraints.NotNull
    private String merchantCode;

    @javax.validation.constraints.NotNull
    private String memberCode;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Controller 代码</p>
<pre><code class="copyable">    @PostMapping("/order/submit")
    public void submit(@RequestBody @Validated OrderRequest request)&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 Postman 发送 Post 请求，并且故意传空的 JSON 串测试，可以看到 Postman 会接受到下面的返回结果：</p>
<pre><code class="copyable">&#123;
    "timestamp": "2021-06-09T11:25:49.136+00:00",
    "status": 400,
    "error": "Bad Request",
    "path": "/order/submit"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这说明注解起作用了，但是这并不是我们希望的结果，我们肯定希望的是能够告诉前端，到底哪个或者哪些字段没有通过校验，并且要知道是什么样的校验没有通过，比如是必传的参数我没传，还是传的数字大于最大限制了等等。</p>
<p>所以下面我们需要对报错信息做处理，在此之前我们需要先知道，这个参数校验的动作其实是 SpringMVC 发出的，具体的校验规则是 hibernate-validator 提供的，可以翻阅 SpringMVC 源码：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f5696092b974bc5a0745bc7b61c9f8a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图中我打断点的地方， SpringMVC 判断是否需要校验，这里面最终是去调用 hibernate-validator 的实现规则，然后下面根据返回的结果，抛出了一个 MethodArgumentNotValidException 类型的异常。这样一来，我们只需要去捕捉这个异常，然后开发者自己做出响应就可以了。捕捉这个异常，我相信大家应该都知道 SpringMVC 统一异常处理</p>
<h2 data-id="heading-3">SpringMVC 统一异常处理</h2>
<p>统一异常处理比较简单，只需要写个类用 @RestControllerAdvice 标注，使用 @ExceptionHandler 标注方法即可，不过 SpringMVC 给我们提供了一个类 ResponseEntityExceptionHandler ，继承它重写 handleExceptionInternal 方法即可</p>
<pre><code class="copyable">@RestControllerAdvice
public class GlobalExceptionController extends ResponseEntityExceptionHandler &#123;
    @Override
    protected ResponseEntity<Object> handleExceptionInternal(Exception ex, Object body, HttpHeaders headers, HttpStatus status, WebRequest request) &#123;
        if(ex instanceof MethodArgumentNotValidException)&#123;
            String message = ((MethodArgumentNotValidException) ex).getFieldErrors().stream().map(v -> v.getField()+":"+v.getDefaultMessage()).collect(Collectors.joining(";"));
            JSONObject obj = new JSONObject();
            obj.put("status",status.value());
            obj.put("error",status.getReasonPhrase());
            obj.put("message",message);
            obj.put("path",((NativeWebRequest) request).getNativeRequest(HttpServletRequest.class).getRequestURI());
            body = obj;
        &#125;
        return super.handleExceptionInternal(ex, body, headers, status, request);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于我们上面看到了，对于不合法的参数校验会抛出 MethodArgumentNotValidException 异常，所以上面我们针对 ex 的类型判断，如果是该类型，把我们需要的信息放进 body 返回给前端，再次使用 Postman 测试，得到以下结果</p>
<pre><code class="copyable">&#123;
    "path": "/order/submit",
    "error": "Bad Request",
    "message": "memberCode:不能为null;merchantCode:不能为null",
    "status": 400
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的结果就是我们通常需要的。那为什么我们重写这个 handleExceptionInternal 方法就能做到拦截异常呢？可以看下我们继承的 ResponseEntityExceptionHandler 类的源码，它自己定义了一个方法用 @ExceptionHandler 标注，并且里面拦截了几乎所有可能发生的异常</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1c0b0c53b024881ba1825b3e346a97a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这些 return 对不同的异常类型做不同处理，但是最终内部调用的都是我们重写的 handleExceptionInternal 方法。</p>
<p>那你可能已经发现了，它只能处理 @ExceptionHandler 中定义好的这些异常类型，开发中我们肯定会自己定义一些异常类，那如何把我们自定义的异常类也捕捉进来呢？</p>
<h2 data-id="heading-4">SpringMVC 处理自定义异常</h2>
<p>仿照 ResponseEntityExceptionHandler 它的写法，我们也写个方法用 @ExceptionHandler 标注即可，首先自定义一个异常类 ClientException</p>
<pre><code class="copyable">public class ClientException extends RuntimeException &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在我们统一处理类中，自定义一个异常处理方法 handleClientException ，加上 @ExceptionHandler 即可</p>
<pre><code class="copyable">@RestControllerAdvice
@Slf4j
public class GlobalExceptionController extends ResponseEntityExceptionHandler &#123;
    @Override
    protected ResponseEntity<Object> handleExceptionInternal(Exception ex, Object body, HttpHeaders headers, HttpStatus status, WebRequest request) &#123;
        if(ex instanceof MethodArgumentNotValidException)&#123;
            String message = ((MethodArgumentNotValidException) ex).getFieldErrors().stream().map(v -> v.getField()+":"+v.getDefaultMessage()).collect(Collectors.joining(";"));
            JSONObject obj = new JSONObject();
            obj.put("status",status.value());
            obj.put("error",status.getReasonPhrase());
            obj.put("message",message);
            obj.put("path",((NativeWebRequest) request).getNativeRequest(HttpServletRequest.class).getRequestURI());

            body = obj;
        &#125; else if (ex instanceof ClientException)&#123;  //捕捉自定义异常
            body = "1111";
        &#125;
        return super.handleExceptionInternal(ex, body, headers, status, request);
    &#125;

    @ExceptionHandler
    public ResponseEntity<Object> handleClientException(ClientException ex, NativeWebRequest request) &#123;
        HttpHeaders headers = new HttpHeaders();
        HttpStatus status = HttpStatus.METHOD_NOT_ALLOWED;
        return handleExceptionInternal(ex, null, headers, status, request);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后我们在代码中测试，抛出一个 ClientException ， 服务器就会响应我们自己定义的信息。</p>
<h2 data-id="heading-5">hibernate-validator 注解功能查询</h2>
<p>如果使用比较少的话，你可能不太熟悉都有哪些注解校验，分别是校验什么功能，所以作为暖男的我在这里把所有校验注解都列出来~~</p>













































































<table><thead><tr><th>注解</th><th>含义</th><th>注解</th><th>含义</th><th>注解</th><th>含义</th></tr></thead><tbody><tr><td><strong>@NotNull</strong></td><td>验证字段不为 null</td><td><strong>@NotEmpty</strong></td><td>验证字段不为空，常用于校验集合元素不为空</td><td><strong>@NotBlank</strong></td><td>验证字段不为空，常用于验证字符串不是空串</td></tr><tr><td><strong>@Max</strong></td><td>验证字段的最大值</td><td><strong>@Min</strong></td><td>验证字段的最小值</td><td><strong>@Digits</strong></td><td>(integer=整数位数, fraction=小数位数)验证字段整数位数和小数位数上限</td></tr><tr><td><strong>@DecimalMax</strong></td><td>与 @Max 类似，不同的是它限定值可以带小数，一般用于 double 和 Bigdecimal 类型</td><td><strong>@DecimalMin</strong></td><td>与 @Min 类似，......</td><td><strong>@Range</strong></td><td>验证数字类型字段值在最小值和最大值之间</td></tr><tr><td><strong>@Size</strong></td><td>验证字段值的在 min 和 max （包含）指定区间之内，如字符长度、集合大小</td><td><strong>@Length</strong></td><td>验证字符串值长度在 min 和 max 区间内</td><td></td><td></td></tr><tr><td><strong>@AssertFalse</strong></td><td>验证布尔类型值是 false</td><td><strong>@AssertTrue</strong></td><td>验证布尔类型值是 true</td><td><strong>@Future</strong></td><td>验证日期类型字段值比当前时间晚</td></tr><tr><td><strong>@Email</strong></td><td>验证字段值是个邮箱</td><td><strong>@Pattern</strong></td><td>(regex=正则表达式) 验证注解的元素值不指定的正则表达式匹配</td><td><strong>@Past</strong></td><td>验证日期类型字段值比当前时间早</td></tr><tr><td><strong>@Negative</strong></td><td>校验必须是负数</td><td><strong>@Positive</strong></td><td>校验必须是正数</td><td><strong>@PastOrPresent</strong></td><td>验证日期类型字段值比当前时间早或者是当前日期</td></tr><tr><td><strong>@NegativeOrZero</strong></td><td>校验必须是负数或 0</td><td><strong>@PositiveOrZero</strong></td><td>校验必须是正数或 0</td><td><strong>@FutureOrPresent</strong></td><td>验证日期类型字段值比当前时间晚或者是当前日期</td></tr></tbody></table>
<h2 data-id="heading-6">校验分组</h2>
<p>实际开发中，我们写一个接受请求参数的类，可能用于多种业务校验。比如我一个类，同时用于保存和更新，那保存一般是不用传 id 的，但是更新时必传 id 字段的。如果我们想用一个类同时满足两种校验怎么办呢？ hibernate-validator 给我们提供了一个分组的方案，我们可以把保存分为一个组，标识哪些字段是保存动作组的，哪些字段是更新动作组的，这样就可以同时满足两种业务的校验需求了。</p>
<p>实际上 hibernate-validator 提供的所有注解都有 groups 属性</p>
<pre><code class="copyable">@Data
public class ReqPremiumLevelRights &#123;

    @NotNull(groups = &#123;UpdateGroup.class&#125;)//只用于更新
    private Long id;
    
    @Length(max = 8, groups = &#123;SaveGroup.class, UpdateGroup.class&#125;)
    @NotNull(groups = &#123;SaveGroup.class, UpdateGroup.class&#125;)
    private String name;
    
    @NotNull(groups = &#123;SaveGroup.class&#125;)
    @Size(min = 1, message = "必须至少选择一个会员权益", groups = &#123;SaveGroup.class, UpdateGroup.class&#125;)
    private List<Long> rightsIds;

    public interface SaveGroup &#123;&#125;
    public interface UpdateGroup &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们在 Controller 里面，使用 @Validated 的时候指定分组就好了</p>
<pre><code class="copyable">    @PostMapping
    @Operation(summary = "新增会员级别(关联权益)")
    public void save(@RequestBody @Validated(ReqPremiumLevelRights.SaveGroup.class) ReqPremiumLevelRights levelRights) &#123;
        premiumMemberLevelService.save(levelRights);
    &#125;

    @PutMapping
    @Operation(summary = "编辑会员级别")
    public void edit(@RequestBody @Validated(ReqPremiumLevelRights.UpdateGroup.class) ReqPremiumLevelRights levelRights) &#123;
        premiumMemberLevelService.update(levelRights);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样一来，就解决了一个类同时用于多种业务校验的问题。</p>
<h2 data-id="heading-7">不依赖 SpringMVC 触发校验动作</h2>
<p>有这样一种场景，我们需要根据某个字段值来确定要使用哪个分组的校验，上面我们是使用不同的接口分开，这样可以自己选择使用哪个分组的规则来校验，如果我们现在要只用一个接口来实现针对不同情况下对不同的分组校验怎么办呢？</p>
<p>举个例子，比如我们现在有个开票需求，针对个人开票有一套校验，针对企业开票有一套校验规则，我们一般不会用两个接口来实现这个开票功能。那么这就要我们在代码中，根据用户类型来自己去决定要使用哪一套校验规则。</p>
<pre><code class="copyable">    @Autowired
    private Validator validator;
    
    @PostMapping
    public void apply(@RequestBody @Validated AppInvoiceApplyRequest request) &#123;
        if (isCorporation) &#123; //企业开票
            validator.validate(request,AppInvoiceApplyRequest.CompanyInvoiceGroup.class);
        &#125; else &#123; //个人开票
            validator.validate(request,AppInvoiceApplyRequest.PersonalCompanyInvoiceGroup.class);
        &#125;
        appInvoiceService.save(request);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实 SpringMVC 源码去调用校验器 validator 的时候也是这么做的，现在我们在参数中，不指定 @Validated 的校验分组，在代码中判断前端传过来的用户类型，根据用户类型使用校验器 validator 去对不同业务对应的校验分组来校验就可以了</p>
<h2 data-id="heading-8">扩展 hibernate-validator 提供的注解</h2>
<p>细心的你可能已经发现了， hibernate-validator 只提供了 20 个左右的校验注解，虽然已经满足了大部分场景的使用，但是由于开发过程中的业务多样性，我们可能会遇到它没有提供的校验需求，比如我们现在要校验一个字段必须是合法的身份证号码，那我们就没有办法了，hibernate-validator 允许我们自己定义注解</p>
<p>首先定义一个校验注解</p>
<pre><code class="copyable">/**
 * 身份证校验
 */
@Target(&#123; ElementType.FIELD&#125;)
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = IdentityConstraintValidator.class)//用哪个校验器校验
public @interface IdentityNo &#123;
    String message() default "身份证号码不符合规则";
    Class<?>[] groups() default &#123; &#125;;
    Class<? extends Payload>[] payload() default &#123; &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>校验逻辑，我们只需要去实现 ConstraintValidator 这个接口重写 isValid 方法即可</p>
<pre><code class="copyable">/**
 * 身份证约束逻辑判断
 */
public class IdentityConstraintValidator implements ConstraintValidator<IdentityNo, String> &#123;
    @Override
    public boolean isValid(String value, ConstraintValidatorContext context) &#123;
        return check(value);//返回身份证号码是否符合规则(自己实现校验逻辑)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样一来，我们自己的注解就定义好了，把它用在需要验证的字段上就可以了。</p>
<pre><code class="copyable">@Data
public class OrderRequest &#123;
    //自己定义的注解
    @IdentityNo
    private String merchantCode;
    private String memberCode;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Postman 测试结果</p>
<pre><code class="copyable">&#123;
    "path": "/order/submit",
    "error": "Bad Request",
    "message": "merchantCode:身份证号码不符合规则",
    "status": 400
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">结语</h2>
<p>hibernate-validator 配合统一异常处理简直是完美呀，这样绝大多数问题在前端传参的时候就能暴露出来了~~</p>
<h3 data-id="heading-10">如果这篇文章对你有帮助，记得点赞加关注。你的支持就是我继续创作的动力</h3></div>  
</div>
            