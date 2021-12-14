
---
title: 'Spring Boot实现各种参数校验，写得太好了'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211209/033058662d92b9dc4f69d99a525dc7e5.png'
author: Dockone
comments: false
date: 2021-12-14 13:15:59
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211209/033058662d92b9dc4f69d99a525dc7e5.png'
---

<div>   
<br>之前也写过一篇关于<code class="prettyprint">Spring Validation</code>使用的文章，不过自我感觉还是浮于表面，本次打算彻底搞懂<code class="prettyprint">Spring Validation</code>。本文会详细介绍<code class="prettyprint">Spring Validation</code>各种场景下的最佳实践及其实现原理，死磕到底！ 项目源码：<a href="https://github.com/chentianming11/spring-validation" rel="nofollow" target="_blank">https://github.com/chentianmin ... ation</a><br>
<h3>简单使用</h3><code class="prettyprint">Java API</code>规范（<code class="prettyprint">JSR303</code>）定义了<code class="prettyprint">Bean</code>校验的标准<code class="prettyprint">validation-api</code>，但没有提供实现。<code class="prettyprint">hibernate validation</code>是对这个规范的实现，并增加了校验注解如<code class="prettyprint">@Email</code>、<code class="prettyprint">@Length</code>等。<code class="prettyprint">Spring Validation</code>是对<code class="prettyprint">hibernate validation</code>的二次封装，用于支持<code class="prettyprint">spring mvc</code>参数自动校验。接下来，我们以<code class="prettyprint">spring-boot</code>项目为例，介绍<code class="prettyprint">Spring Validation</code>的使用。<br>
<h4>引入依赖</h4>如果<code class="prettyprint">spring-boot</code>版本小于<code class="prettyprint">2.3.x</code>，<code class="prettyprint">spring-boot-starter-web</code>会自动传入<code class="prettyprint">hibernate-validator</code>依赖。如果<code class="prettyprint">spring-boot</code>版本大于<code class="prettyprint">2.3.x</code>，则需要手动引入依赖：<br>
<pre class="prettyprint"><dependency><br>
<groupId>org.hibernate</groupId><br>
<artifactId>hibernate-validator</artifactId><br>
<version>6.0.1.Final</version><br>
</dependency><br>
</pre><br>
对于<code class="prettyprint">Web</code>服务来说，为防止非法参数对业务造成影响，在<code class="prettyprint">Controller</code>层一定要做参数校验的！大部分情况下，请求参数分为如下两种形式：<br>
<ol><li><code class="prettyprint">POST</code>、<code class="prettyprint">PUT</code>请求，使用<code class="prettyprint">requestBody</code>传递参数；</li><li><code class="prettyprint">GET</code>请求，使用<code class="prettyprint">requestParam/PathVariable</code>传递参数。</li></ol><br>
<br>下面我们简单介绍下<code class="prettyprint">requestBody</code>和<code class="prettyprint">requestParam/PathVariable</code>的参数校验实战！<br>
<h4><code class="prettyprint">requestBody</code>参数校验</h4><code class="prettyprint">POST</code>、<code class="prettyprint">PUT</code>请求一般会使用<code class="prettyprint">requestBody</code>传递参数，这种情况下，后端使用<strong>DTO对象</strong>进行接收。只要给DTO对象加上<code class="prettyprint">@Validated</code>注解就能实现自动参数校验。比如，有一个保存<code class="prettyprint">User</code>的接口，要求<code class="prettyprint">userName</code>长度是<code class="prettyprint">2-10</code>，<code class="prettyprint">account</code>和<code class="prettyprint">password</code>字段长度是<code class="prettyprint">6-20</code>。如果校验失败，会抛出<code class="prettyprint">MethodArgumentNotValidException</code>异常，<code class="prettyprint">Spring</code>默认会将其转为<code class="prettyprint">400（Bad Request）</code>请求。<br>
<br>DTO表示数据传输对象（Data Transfer Object），用于服务器和客户端之间交互传输使用的。在spring-web项目中可以表示用于接收请求参数的<code class="prettyprint">Bean</code>对象。<br>
<br>在<code class="prettyprint">DTO</code>字段上声明约束注解：<br>
<pre class="prettyprint">@Data<br>
public class UserDTO &#123;<br>
<br>
private Long userId;<br>
<br>
@NotNull<br>
@Length(min = 2, max = 10)<br>
private String userName;<br>
<br>
@NotNull<br>
@Length(min = 6, max = 20)<br>
private String account;<br>
<br>
@NotNull<br>
@Length(min = 6, max = 20)<br>
private String password;<br>
&#125; <br>
</pre><br>
在方法参数上声明校验注解：<br>
<pre class="prettyprint">@PostMapping("/save")<br>
public Result saveUser(@RequestBody @Validated UserDTO userDTO) &#123;<br>
// 校验通过，才会执行业务逻辑处理<br>
return Result.ok();<br>
&#125; <br>
</pre><br>
这种情况下，<strong>使用<code class="prettyprint">@Valid</code>和<code class="prettyprint">@Validated</code>都可以</strong>。<br>
<h4><code class="prettyprint">requestParam/PathVariable</code>参数校验</h4><code class="prettyprint">GET</code>请求一般会使用<code class="prettyprint">requestParam/PathVariable</code>传参。如果参数比较多（比如超过6个），还是推荐使用<code class="prettyprint">DTO</code>对象接收。否则，推荐将一个个参数平铺到方法入参中。在这种情况下，必须在<code class="prettyprint">Controller</code>类上标注<code class="prettyprint">@Validated</code>注解，并在入参上声明约束注解（如<code class="prettyprint">@Min</code>等）。如果校验失败，会抛出<code class="prettyprint">ConstraintViolationException</code>异常。代码示例如下：<br>
<pre class="prettyprint">@RequestMapping("/api/user")<br>
@RestController<br>
@Validated<br>
public class UserController &#123;<br>
// 路径变量<br>
@GetMapping("&#123;userId&#125;")<br>
public Result detail(@PathVariable("userId") @Min(10000000000000000L) Long userId) &#123;<br>
    // 校验通过，才会执行业务逻辑处理<br>
    UserDTO userDTO = new UserDTO();<br>
    userDTO.setUserId(userId);<br>
    userDTO.setAccount("11111111111111111");<br>
    userDTO.setUserName("xixi");<br>
    userDTO.setAccount("11111111111111111");<br>
    return Result.ok(userDTO);<br>
&#125;<br>
<br>
// 查询参数<br>
@GetMapping("getByAccount")<br>
public Result getByAccount(@Length(min = 6, max = 20) @NotNull String  account) &#123;<br>
    // 校验通过，才会执行业务逻辑处理<br>
    UserDTO userDTO = new UserDTO();<br>
    userDTO.setUserId(10000000000000003L);<br>
    userDTO.setAccount(account);<br>
    userDTO.setUserName("xixi");<br>
    userDTO.setAccount("11111111111111111");<br>
    return Result.ok(userDTO);<br>
&#125;<br>
&#125; <br>
</pre><br>
<h4>统一异常处理</h4>前面说过，如果校验失败，会抛出<code class="prettyprint">MethodArgumentNotValidException</code>或者<code class="prettyprint">ConstraintViolationException</code>异常。在实际项目开发中，通常会用<strong>统一异常处理</strong>来返回一个更友好的提示。比如我们系统要求无论发送什么异常，<code class="prettyprint">http</code>的状态码必须返回<code class="prettyprint">200</code>，由业务码去区分系统的异常情况。<br>
<pre class="prettyprint">@RestControllerAdvice<br>
public class CommonExceptionHandler &#123;<br>
<br>
@ExceptionHandler(&#123;MethodArgumentNotValidException.class&#125;)<br>
@ResponseStatus(HttpStatus.OK)<br>
@ResponseBody<br>
public Result handleMethodArgumentNotValidException(MethodArgumentNotValidException ex) &#123;<br>
    BindingResult bindingResult = ex.getBindingResult();<br>
    StringBuilder sb = new StringBuilder("校验失败:");<br>
    for (FieldError fieldError : bindingResult.getFieldErrors()) &#123;<br>
        sb.append(fieldError.getField()).append("：").append(fieldError.getDefaultMessage()).append(", ");<br>
    &#125;<br>
    String msg = sb.toString();<br>
   return Result.fail(BusinessCode.参数校验失败, msg);<br>
&#125;<br>
<br>
@ExceptionHandler(&#123;ConstraintViolationException.class&#125;)<br>
@ResponseStatus(HttpStatus.OK)<br>
@ResponseBody<br>
public Result handleConstraintViolationException(ConstraintViolationException ex) &#123;<br>
    return Result.fail(BusinessCode.参数校验失败, ex.getMessage());<br>
&#125;<br>
&#125; <br>
</pre><br>
<h3>进阶使用</h3><h4>分组校验</h4>在实际项目中，可能多个方法需要使用同一个<code class="prettyprint">DTO</code>类来接收参数，而不同方法的校验规则很可能是不一样的。这个时候，简单地在<code class="prettyprint">DTO</code>类的字段上加约束注解无法解决这个问题。因此，<code class="prettyprint">spring-validation</code>支持了<strong>分组校验</strong>的功能，专门用来解决这类问题。还是上面的例子，比如保存<code class="prettyprint">User</code>的时候，<code class="prettyprint">UserId</code>是可空的，但是更新<code class="prettyprint">User</code>的时候，<code class="prettyprint">UserId</code>的值必须<code class="prettyprint">>=10000000000000000L</code>；其它字段的校验规则在两种情况下一样。这个时候使用<strong>分组校验</strong>的代码示例如下：<br>
<br>约束注解上声明适用的分组信息<code class="prettyprint">groups</code>：<br>
<pre class="prettyprint">@Data<br>
public class UserDTO &#123;<br>
<br>
@Min(value = 10000000000000000L, groups = Update.class)<br>
private Long userId;<br>
<br>
@NotNull(groups = &#123;Save.class, Update.class&#125;)<br>
@Length(min = 2, max = 10, groups = &#123;Save.class, Update.class&#125;)<br>
private String userName;<br>
<br>
@NotNull(groups = &#123;Save.class, Update.class&#125;)<br>
@Length(min = 6, max = 20, groups = &#123;Save.class, Update.class&#125;)<br>
private String account;<br>
<br>
@NotNull(groups = &#123;Save.class, Update.class&#125;)<br>
@Length(min = 6, max = 20, groups = &#123;Save.class, Update.class&#125;)<br>
private String password;<br>
<br>
/**<br>
 * 保存的时候校验分组<br>
 */<br>
public interface Save &#123;<br>
&#125;<br>
<br>
/**<br>
 * 更新的时候校验分组<br>
 */<br>
public interface Update &#123;<br>
&#125;<br>
&#125; <br>
</pre><br>
<code class="prettyprint">@Validated</code>注解上指定校验分组：<br>
<pre class="prettyprint">@PostMapping("/save")<br>
public Result saveUser(@RequestBody @Validated(UserDTO.Save.class) UserDTO userDTO) &#123;<br>
// 校验通过，才会执行业务逻辑处理<br>
return Result.ok();<br>
&#125;<br>
<br>
@PostMapping("/update")<br>
public Result updateUser(@RequestBody @Validated(UserDTO.Update.class) UserDTO userDTO) &#123;<br>
// 校验通过，才会执行业务逻辑处理<br>
return Result.ok();<br>
&#125; <br>
</pre><br>
<h4>嵌套校验</h4>前面的示例中，<code class="prettyprint">DTO</code>类里面的字段都是<code class="prettyprint">基本数据类型</code>和<code class="prettyprint">String</code>类型。但是实际场景中，有可能某个字段也是一个对象，这种情况先，可以使用<code class="prettyprint">嵌套校验</code>。比如，上面保存<code class="prettyprint">User</code>信息的时候同时还带有<code class="prettyprint">Job</code>信息。需要注意的是，此时<code class="prettyprint">DTO</code>类的对应字段必须标记<code class="prettyprint">@Valid</code>注解。<br>
<pre class="prettyprint">@Data<br>
public class UserDTO &#123;<br>
<br>
@Min(value = 10000000000000000L, groups = Update.class)<br>
private Long userId;<br>
<br>
@NotNull(groups = &#123;Save.class, Update.class&#125;)<br>
@Length(min = 2, max = 10, groups = &#123;Save.class, Update.class&#125;)<br>
private String userName;<br>
<br>
@NotNull(groups = &#123;Save.class, Update.class&#125;)<br>
@Length(min = 6, max = 20, groups = &#123;Save.class, Update.class&#125;)<br>
private String account;<br>
<br>
@NotNull(groups = &#123;Save.class, Update.class&#125;)<br>
@Length(min = 6, max = 20, groups = &#123;Save.class, Update.class&#125;)<br>
private String password;<br>
<br>
@NotNull(groups = &#123;Save.class, Update.class&#125;)<br>
@Valid<br>
private Job job;<br>
<br>
@Data<br>
public static class Job &#123;<br>
<br>
    @Min(value = 1, groups = Update.class)<br>
    private Long jobId;<br>
<br>
    @NotNull(groups = &#123;Save.class, Update.class&#125;)<br>
    @Length(min = 2, max = 10, groups = &#123;Save.class, Update.class&#125;)<br>
    private String jobName;<br>
<br>
    @NotNull(groups = &#123;Save.class, Update.class&#125;)<br>
    @Length(min = 2, max = 10, groups = &#123;Save.class, Update.class&#125;)<br>
    private String position;<br>
&#125;<br>
<br>
/**<br>
 * 保存的时候校验分组<br>
 */<br>
public interface Save &#123;<br>
&#125;<br>
<br>
/**<br>
 * 更新的时候校验分组<br>
 */<br>
public interface Update &#123;<br>
&#125;<br>
&#125; <br>
</pre><br>
嵌套校验可以结合分组校验一起使用。还有就是<code class="prettyprint">嵌套集合校验</code>会对集合里面的每一项都进行校验，例如<code class="prettyprint">List&lt;Job></code>字段会对这个<code class="prettyprint">list</code>里面的每一个<code class="prettyprint">Job</code>对象都进行校验。<br>
<h4>集合校验</h4>如果请求体直接传递了<code class="prettyprint">json</code>数组给后台，并希望对数组中的每一项都进行参数校验。此时，如果我们直接使用<code class="prettyprint">java.util.Collection</code>下的<code class="prettyprint">list</code>或者<code class="prettyprint">set</code>来接收数据，参数校验并不会生效！我们可以使用自定义<code class="prettyprint">list</code>集合来接收参数：<br>
<br>包装<code class="prettyprint">List</code>类型，并声明<code class="prettyprint">@Valid</code>注解：<br>
<pre class="prettyprint">public class ValidationList<E> implements List<E> &#123;<br>
<br>
@Delegate // @Delegate是lombok注解<br>
@Valid // 一定要加@Valid注解<br>
public List<E> list = new ArrayList<>();<br>
<br>
// 一定要记得重写toString方法<br>
@Override<br>
public String toString() &#123;<br>
    return list.toString();<br>
&#125;<br>
&#125; <br>
</pre><br>
<code class="prettyprint">@Delegate</code>注解受<code class="prettyprint">lombok</code>版本限制，<code class="prettyprint">1.18.6</code>以上版本可支持。如果校验不通过，会抛出<code class="prettyprint">NotReadablePropertyException</code>，同样可以使用统一异常进行处理。<br>
<br>比如，我们需要一次性保存多个<code class="prettyprint">User</code>对象，<code class="prettyprint">Controller</code>层的方法可以这么写：<br>
<pre class="prettyprint">@PostMapping("/saveList")<br>
public Result saveList(@RequestBody @Validated(UserDTO.Save.class) ValidationList<UserDTO> userList) &#123;<br>
// 校验通过，才会执行业务逻辑处理<br>
return Result.ok();<br>
&#125; <br>
</pre><br>
<h4>自定义校验</h4>业务需求总是比框架提供的这些简单校验要复杂的多，我们可以自定义校验来满足我们的需求。自定义<code class="prettyprint">spring validation</code>非常简单，假设我们自定义<code class="prettyprint">加密id</code>（由数字或者<code class="prettyprint">a-f</code>的字母组成，<code class="prettyprint">32-256</code>长度）校验，主要分为两步：<br>
<br>自定义约束注解：<br>
<pre class="prettyprint">@Target(&#123;METHOD, FIELD, ANNOTATION_TYPE, CONSTRUCTOR, PARAMETER&#125;)<br>
@Retention(RUNTIME)<br>
@Documented<br>
@Constraint(validatedBy = &#123;EncryptIdValidator.class&#125;)<br>
public @interface EncryptId &#123;<br>
<br>
// 默认错误消息<br>
String message() default "加密id格式错误";<br>
<br>
// 分组<br>
Class<?>[] groups() default &#123;&#125;;<br>
<br>
// 负载<br>
Class<? extends Payload>[] payload() default &#123;&#125;;<br>
&#125; <br>
</pre><br>
实现<code class="prettyprint">ConstraintValidator</code>接口编写约束校验器：<br>
<pre class="prettyprint">public class EncryptIdValidator implements ConstraintValidator<EncryptId, String> &#123;<br>
<br>
private static final Pattern PATTERN = Pattern.compile("^[a-f\\d]&#123;32,256&#125;$");<br>
<br>
@Override<br>
public boolean isValid(String value, ConstraintValidatorContext context) &#123;<br>
    // 不为null才进行校验<br>
    if (value != null) &#123;<br>
        Matcher matcher = PATTERN.matcher(value);<br>
        return matcher.find();<br>
    &#125;<br>
    return true;<br>
&#125;<br>
&#125; <br>
</pre><br>
这样我们就可以使用<code class="prettyprint">@EncryptId</code>进行参数校验了！<br>
<h4>编程式校验</h4>上面的示例都是基于<code class="prettyprint">注解</code>来实现自动校验的，在某些情况下，我们可能希望以<code class="prettyprint">编程方式</code>调用验证。这个时候可以注入<code class="prettyprint">javax.validation.Validator</code>对象，然后再调用其<code class="prettyprint">api</code>。<br>
<pre class="prettyprint">@Autowired<br>
private javax.validation.Validator globalValidator;<br>
<br>
// 编程式校验<br>
@PostMapping("/saveWithCodingValidate")<br>
public Result saveWithCodingValidate(@RequestBody UserDTO userDTO) &#123;<br>
Set<ConstraintViolation<UserDTO>> validate = globalValidator.validate(userDTO, UserDTO.Save.class);<br>
// 如果校验通过，validate为空；否则，validate包含未校验通过项<br>
if (validate.isEmpty()) &#123;<br>
    // 校验通过，才会执行业务逻辑处理<br>
<br>
&#125; else &#123;<br>
    for (ConstraintViolation<UserDTO> userDTOConstraintViolation : validate) &#123;<br>
        // 校验失败，做其它逻辑<br>
        System.out.println(userDTOConstraintViolation);<br>
    &#125;<br>
&#125;<br>
return Result.ok();<br>
&#125; <br>
</pre><br>
<h4>快速失败（Fail Fast）</h4><code class="prettyprint">Spring Validation</code>默认会校验完所有字段，然后才抛出异常。可以通过一些简单的配置，开启<code class="prettyprint">Fali Fast</code>模式，一旦校验失败就立即返回。<br>
<pre class="prettyprint">@Bean<br>
public Validator validator() &#123;<br>
ValidatorFactory validatorFactory = Validation.byProvider(HibernateValidator.class)<br>
        .configure()<br>
        // 快速失败模式<br>
        .failFast(true)<br>
        .buildValidatorFactory();<br>
return validatorFactory.getValidator();<br>
&#125; <br>
</pre><br>
<h4><code class="prettyprint">@Valid</code>和<code class="prettyprint">@Validated</code>区别</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211209/033058662d92b9dc4f69d99a525dc7e5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211209/033058662d92b9dc4f69d99a525dc7e5.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>实现原理</h3><h4><code class="prettyprint">requestBody</code>参数校验实现原理</h4>在<code class="prettyprint">spring-mvc</code>中，<code class="prettyprint">RequestResponseBodyMethodProcessor</code>是用于解析<code class="prettyprint">@RequestBody</code>标注的参数以及处理<code class="prettyprint">@ResponseBody</code>标注方法的返回值的。显然，执行参数校验的逻辑肯定就在解析参数的方法<code class="prettyprint">resolveArgument()</code>中：<br>
<pre class="prettyprint">public class RequestResponseBodyMethodProcessor extends AbstractMessageConverterMethodProcessor &#123;<br>
@Override<br>
public Object resolveArgument(MethodParameter parameter, @Nullable ModelAndViewContainer mavContainer,<br>
                              NativeWebRequest webRequest, @Nullable WebDataBinderFactory binderFactory) throws Exception &#123;<br>
<br>
    parameter = parameter.nestedIfOptional();<br>
    //将请求数据封装到DTO对象中<br>
    Object arg = readWithMessageConverters(webRequest, parameter, parameter.getNestedGenericParameterType());<br>
    String name = Conventions.getVariableNameForParameter(parameter);<br>
<br>
    if (binderFactory != null) &#123;<br>
        WebDataBinder binder = binderFactory.createBinder(webRequest, arg, name);<br>
        if (arg != null) &#123;<br>
            // 执行数据校验<br>
            validateIfApplicable(binder, parameter);<br>
            if (binder.getBindingResult().hasErrors() && isBindExceptionRequired(binder, parameter)) &#123;<br>
                throw new MethodArgumentNotValidException(parameter, binder.getBindingResult());<br>
            &#125;<br>
        &#125;<br>
        if (mavContainer != null) &#123;<br>
            mavContainer.addAttribute(BindingResult.MODEL_KEY_PREFIX + name, binder.getBindingResult());<br>
        &#125;<br>
    &#125;<br>
    return adaptArgumentIfNecessary(arg, parameter);<br>
&#125;<br>
&#125; <br>
</pre><br>
可以看到，<code class="prettyprint">resolveArgument()</code>调用了<code class="prettyprint">validateIfApplicable()</code>进行参数校验。<br>
<pre class="prettyprint">protected void validateIfApplicable(WebDataBinder binder, MethodParameter parameter) &#123;<br>
// 获取参数注解，比如@RequestBody、@Valid、@Validated<br>
Annotation[] annotations = parameter.getParameterAnnotations();<br>
for (Annotation ann : annotations) &#123;<br>
    // 先尝试获取@Validated注解<br>
    Validated validatedAnn = AnnotationUtils.getAnnotation(ann, Validated.class);<br>
    //如果直接标注了@Validated，那么直接开启校验。<br>
    //如果没有，那么判断参数前是否有Valid起头的注解。<br>
    if (validatedAnn != null || ann.annotationType().getSimpleName().startsWith("Valid")) &#123;<br>
        Object hints = (validatedAnn != null ? validatedAnn.value() : AnnotationUtils.getValue(ann));<br>
        Object[] validationHints = (hints instanceof Object[] ? (Object[]) hints : new Object[] &#123;hints&#125;);<br>
        //执行校验<br>
        binder.validate(validationHints);<br>
        break;<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
看到这里，大家应该能明白为什么这种场景下<code class="prettyprint">@Validated</code>、<code class="prettyprint">@Valid</code>两个注解可以混用。我们接下来继续看<code class="prettyprint">WebDataBinder.validate()</code>实现。<br>
<pre class="prettyprint">@Override<br>
public void validate(Object target, Errors errors, Object... validationHints) &#123;<br>
if (this.targetValidator != null) &#123;<br>
    processConstraintViolations(<br>
        //此处调用Hibernate Validator执行真正的校验<br>
        this.targetValidator.validate(target, asValidationGroups(validationHints)), errors);<br>
&#125;<br>
&#125; <br>
</pre><br>
最终发现底层最终还是调用了<code class="prettyprint">Hibernate Validator</code>进行真正的校验处理。<br>
<h4>方法级别的参数校验实现原理</h4>上面提到的将参数一个个平铺到方法参数中，然后在每个参数前面声明<code class="prettyprint">约束注解</code>的校验方式，就是方法级别的参数校验。实际上，这种方式可用于任何<code class="prettyprint">Spring Bean</code>的方法上，比如<code class="prettyprint">Controller</code>/<code class="prettyprint">Service</code>等。其底层实现原理就是<code class="prettyprint">AOP</code>，具体来说是通过<code class="prettyprint">MethodValidationPostProcessor</code>动态注册<code class="prettyprint">AOP</code>切面，然后使用<code class="prettyprint">MethodValidationInterceptor</code>对切点方法织入增强。<br>
<pre class="prettyprint">public class MethodValidationPostProcessor extends AbstractBeanFactoryAwareAdvisingPostProcessorimplements InitializingBean &#123;<br>
@Override<br>
public void afterPropertiesSet() &#123;<br>
    //为所有`@Validated`标注的Bean创建切面<br>
    Pointcut pointcut = new AnnotationMatchingPointcut(this.validatedAnnotationType, true);<br>
    //创建Advisor进行增强<br>
    this.advisor = new DefaultPointcutAdvisor(pointcut, createMethodValidationAdvice(this.validator));<br>
&#125;<br>
<br>
//创建Advice，本质就是一个方法拦截器<br>
protected Advice createMethodValidationAdvice(@Nullable Validator validator) &#123;<br>
    return (validator != null ? new MethodValidationInterceptor(validator) : new MethodValidationInterceptor());<br>
&#125;<br>
&#125; <br>
</pre><br>
接着看一下<code class="prettyprint">MethodValidationInterceptor</code>：<br>
<pre class="prettyprint">public class MethodValidationInterceptor implements MethodInterceptor &#123;<br>
@Override<br>
public Object invoke(MethodInvocation invocation) throws Throwable &#123;<br>
    //无需增强的方法，直接跳过<br>
    if (isFactoryBeanMetadataMethod(invocation.getMethod())) &#123;<br>
        return invocation.proceed();<br>
    &#125;<br>
    //获取分组信息<br>
    Class<?>[] groups = determineValidationGroups(invocation);<br>
    ExecutableValidator execVal = this.validator.forExecutables();<br>
    Method methodToValidate = invocation.getMethod();<br>
    Set<ConstraintViolation<Object>> result;<br>
    try &#123;<br>
        //方法入参校验，最终还是委托给Hibernate Validator来校验<br>
        result = execVal.validateParameters(<br>
            invocation.getThis(), methodToValidate, invocation.getArguments(), groups);<br>
    &#125;<br>
    catch (IllegalArgumentException ex) &#123;<br>
        ...<br>
    &#125;<br>
    //有异常直接抛出<br>
    if (!result.isEmpty()) &#123;<br>
        throw new ConstraintViolationException(result);<br>
    &#125;<br>
    //真正的方法调用<br>
    Object returnValue = invocation.proceed();<br>
    //对返回值做校验，最终还是委托给Hibernate Validator来校验<br>
    result = execVal.validateReturnValue(invocation.getThis(), methodToValidate, returnValue, groups);<br>
    //有异常直接抛出<br>
    if (!result.isEmpty()) &#123;<br>
        throw new ConstraintViolationException(result);<br>
    &#125;<br>
    return returnValue;<br>
&#125;<br>
&#125; <br>
</pre><br>
实际上，不管是<code class="prettyprint">requestBody参数校验</code>还是<code class="prettyprint">方法级别的校验</code>，最终都是调用<code class="prettyprint">Hibernate Validator</code>执行校验，<code class="prettyprint">Spring Validation</code>只是做了一层封装。<br>
<br>原文链接：<a href="https://juejin.cn/post/6856541106626363399" rel="nofollow" target="_blank">https://juejin.cn/post/6856541106626363399</a>，作者：夜尽天明_
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            