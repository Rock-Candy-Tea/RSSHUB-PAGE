
---
title: 'DDD代码整洁之道'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=527'
author: 掘金
comments: false
date: Fri, 30 Apr 2021 05:15:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=527'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在实现DDD的过程中，我们需要严格遵守代码规范才能保持代码的整洁，否则随着需求的迭代，项目很容易就失去DDD该有的模样，变得即不DDD也不MVC。</p>
<h2 data-id="heading-0">应用服务、领域服务、聚合根、资源库的职责</h2>
<p>资源库（Repository）的职责是提供聚合根或者持久化聚合根，除此之外应尽可能的没有其它行为，否则聚合根就会严重退化成DAO。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Repository</span><<span class="hljs-title">DO</span>, <span class="hljs-title">KEY</span>> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">save</span><span class="hljs-params">(DO obj)</span></span>;
    <span class="hljs-function">DO <span class="hljs-title">findById</span><span class="hljs-params">(KEY id)</span></span>;
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">deleteById</span><span class="hljs-params">(KEY id)</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>聚合根则封装业务操作，聚合根下实体的业务操作也应该通过聚合根完成，即应用服务（ApplicationService）与领域服务（DomainService）都不可绕过聚合根调用实体的业务方法，必须通过聚合根去调用。</p>
<p>应用服务是业务逻辑的封装，不处理业务逻辑。虽然领域服务不是必须的，但对于不能直接通过聚合根完成的业务操作就需要通过领域服务。</p>
<p>如修改用户信息，可在应用服务通过资源库获取用户聚合根，再调用用户聚合根的修改用户信息方法，最后通过资源库持久化用户聚合根。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserApplicationService</span></span>&#123;

    <span class="hljs-comment">/**
     * 更新用户基本信息
     *
     * <span class="hljs-doctag">@param</span> command
     * <span class="hljs-doctag">@param</span> token
     */</span>
    <span class="hljs-meta">@Transactional(rollbackFor = Throwable.class, isolation = Isolation.READ_COMMITTED)</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">updateUserInfo</span><span class="hljs-params">(ModifyUserInfoCommand command, String token)</span> </span>&#123;
        <span class="hljs-comment">// 获取聚合根</span>
        Account account = findByAccountId(getUser(token).getId());
        <span class="hljs-comment">// 调用业务方法</span>
        account.modifyAccountInfo(AccountInfoValobj.builder()
                .nickname(command.getNickname())
                .avatarUrl(command.getAvatarUrl())
                .country(command.getCountry())
                .province(command.getProvince())
                .city(command.getCity())
                .gender(Sex.valueBy(command.getGender()))
                .build());
        <span class="hljs-comment">// 通过资源库持久化</span>
        repository.save(account);
        <span class="hljs-comment">// 更新缓存</span>
        accountCache.cache(token, getUserById(account.getId()));
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里用户聚合根能到看到自己的信息，用户自己修改自己的信息可直接通过聚合根完成，因此这种场景下我们不需要领域服务。</p>
<p>复杂场景如用户绑定手机号码就不能直接在领域服务中完成。</p>
<p>绑定手机号码一般流程为：获取短信验证码、校验短信验证码、校验手机号码是否已经绑定了别的账号。</p>
<p>其中获取短信验证码与校验短信验证码应放在应用服务完成，而校验手机号码是否已经绑定了别的账号就需要由领域服务完成，因为聚合根无法完成这个判断， 聚合根看不到别的账号，聚合根不能拥有资源库。</p>
<p>聚合根</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Account</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">BaseAggregate</span><<span class="hljs-title">AccountEvent</span>></span>&#123;
    <span class="hljs-comment">// .....</span>
    <span class="hljs-keyword">private</span> String phone;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">bindMobilePhone</span><span class="hljs-params">(String phoneNumber)</span> </span>&#123;
        <span class="hljs-keyword">if</span> (!StringUtils.isEmpty(<span class="hljs-keyword">this</span>.phone)) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> AccountParamException(<span class="hljs-string">"已经绑定过手机号码了，如需更新可走更换手机号码流程"</span>);
        &#125;
        <span class="hljs-keyword">this</span>.phone = phoneNumber;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>领域服务</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Service</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AccountDomainService</span> </span>&#123;
    
    <span class="hljs-keyword">private</span> AccountRepository repository;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">AccountDomainService</span><span class="hljs-params">(AccountRepository repository)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.repository = repository;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">bindMobilePhone</span><span class="hljs-params">(Long userId, String phone)</span> </span>&#123;
        Account account = repository.findById(userId);
        <span class="hljs-keyword">if</span> (account == <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> AccountNotFoundException(userId);
        &#125;
        <span class="hljs-comment">// 号码被其它账户绑定了</span>
        <span class="hljs-keyword">boolean</span> exist = repository.findByPhone(phone) != <span class="hljs-keyword">null</span>;
        <span class="hljs-keyword">if</span> (exist) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> AccountBindPhoneException(phone);
        &#125;
        account.bindMobilePhone(phone);
        repository.save(account);
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>应用服务</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Service</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserApplicationService</span> </span>&#123;
    
       <span class="hljs-comment">/**
         * 绑定手机号码-发送验证码
         *
         * <span class="hljs-doctag">@param</span> command
         * <span class="hljs-doctag">@param</span> token
         */</span>
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">bindMobilePhoneSendVerifyCode</span><span class="hljs-params">(VerifyCodeSendCommand command, String token)</span> </span>&#123;
            <span class="hljs-comment">// verify login</span>
            getUser(token);
            String key = String.format(CacheKeyConstants.BIND_PHONE_VERIFY_CODE, command.getPhone());
            <span class="hljs-comment">// 生成验证码</span>
            String verifyCode = ValidCodeUtils.generateNumberValidCode(<span class="hljs-number">4</span>);
            <span class="hljs-comment">// 过期时间三分钟</span>
            redisTemplate.opsForValue().set(key, verifyCode, <span class="hljs-number">180</span>, TimeUnit.SECONDS);
            <span class="hljs-comment">// 调用消息服务发送验证码</span>
            messageClientGateway.sendSmsVerifyCode(command.getPhone(), verifyCode);
        &#125;
    
        <span class="hljs-comment">/**
         * 绑定手机号码-提交绑定
         *
         * <span class="hljs-doctag">@param</span> command
         * <span class="hljs-doctag">@param</span> token
         */</span>
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">bindMobilePhone</span><span class="hljs-params">(BindPhoneCommand command, String token)</span> </span>&#123;
            <span class="hljs-comment">// 校验验证码</span>
            String key = String.format(CacheKeyConstants.BIND_PHONE_VERIFY_CODE, command.getPhone());
            String verifyCode = redisTemplate.opsForValue().get(key);
            <span class="hljs-keyword">if</span> (!command.getVerifyCode().equalsIgnoreCase(verifyCode)) &#123;
                <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> VerifyPhoneCodeApplicationException();
            &#125;
            Long userId = getUser(token).getId();
            <span class="hljs-comment">// 通过领域服务绑定手机号码</span>
            accountDomainService.bindMobilePhone(userId, command.getPhone());
            <span class="hljs-comment">// 更新缓存</span>
            accountCache.cache(token, getUserById(userId));
        &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接口层</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@RestController</span>
<span class="hljs-meta">@RequestMapping("account")</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserController</span> </span>&#123;
 
    <span class="hljs-meta">@Resource</span>
    <span class="hljs-keyword">private</span> UserApplicationService userApplicationService;

    <span class="hljs-meta">@ApiOperation("绑定手机号-获取验证码")</span>
    <span class="hljs-meta">@GetMapping("/bindMobilePhone/verifyCode")</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Response<Void> <span class="hljs-title">bindMobilePhone</span><span class="hljs-params">(<span class="hljs-meta">@RequestParam("phone")</span> String phone, 
                HttpServletRequest request)</span> </span>&#123;
        String token = request.getHeader(Constants.AUTHENTICATION_TOKEN);
        userApplicationService.bindMobilePhoneSendVerifyCode(phone, token);
        <span class="hljs-keyword">return</span> Response.success();
    &#125;

    <span class="hljs-meta">@ApiOperation("绑定手机号-提交绑定")</span>
    <span class="hljs-meta">@PostMapping("/bindMobilePhone/submit")</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Response<Void> <span class="hljs-title">bindMobilePhone</span><span class="hljs-params">(<span class="hljs-meta">@RequestBody</span> <span class="hljs-meta">@Validated</span> BindPhoneCommand command,
                 HttpServletRequest request)</span> </span>&#123;
        String token = request.getHeader(Constants.AUTHENTICATION_TOKEN);
        userApplicationService.bindMobilePhone(command, token);
        <span class="hljs-keyword">return</span> Response.success();
    &#125;
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">严格遵守CQRS</h2>
<p>所有写操作必须走“应用服务-资源库-聚合根-资源库”流程，即应用服务封装一次业务操作，应用服务通过资源库获取聚合根，调用聚合根的业务方法，最后调用资源库持久化聚合根。如果有产生领域事件则最后由应用服务发布事件。</p>
<p>复杂场景下走“应用服务-领域服务-资源库-聚合根-资源库”流程，即应用服务完成应用层的封装，由领域服务封装对聚合根的操作以及一些聚合根无法完成的业务逻辑。</p>
<p>所有读操作都必须走反模式的（Services-->Dao），包括查询单个聚合根的详情、分页查询等场景。</p>
<p>接口层</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@RequestMapping("/order")</span>
<span class="hljs-meta">@RestController</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">OrderController</span> </span>&#123;
    
    <span class="hljs-meta">@GetMapping("/query")</span>
    <span class="hljs-keyword">public</span> Response<PageInfo<OrderListRepresentation>> queryOrder(OrderQuery query, HttpServletRequest request) &#123;
        <span class="hljs-keyword">return</span> Response.success(orderRepresentationService.listByOrderStatus(query,
                request.getHeader(Constants.AUTHENTICATION_TOKEN)));
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>应用层</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Service</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">OrderRepresentationService</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Cqrs</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-keyword">public</span> PageInfo<OrderListRepresentation> <span class="hljs-title">queryOrder</span><span class="hljs-params">(OrderQuery query, String token)</span> </span>&#123;
        Long merchantId = merchantApplicationServiceGateway.loginMerchantUser(token).getMerchantId();
        IPage<OrderListRepresentation> orderPage = <span class="hljs-keyword">new</span> Page<>(query.getPage(), query.getPageSize());
        List<OrderListRepresentation> orders = exploreShopOrderMapper.selectOrderBy(merchantId,query,orderPage);
        PageInfo<OrderListRepresentation> pageInfo = <span class="hljs-keyword">new</span> PageInfo<>(page, pageSize);
        pageInfo.setTotalCount((<span class="hljs-keyword">int</span>) orderPage.getTotal());
        <span class="hljs-keyword">if</span> (CollectionUtils.isEmpty(orders)) &#123;
            pageInfo.setList(Collections.emptyList());
        &#125; <span class="hljs-keyword">else</span> &#123;
            orders.parallelStream().forEach(order -> &#123;
                order.setStatusName(OrderStatus.valueOf(order.getStatus()).getName());
                List<Platform> platforms = Arrays.stream(order.getPlatformIds().split(<span class="hljs-string">","</span>))
                        .map(Integer::parseInt)
                        .map(Platform::valueOf)
                        .collect(Collectors.toList());
                order.setPlatforms(platforms.stream().map(Platform::getValue).collect(Collectors.toList()));
                order.setPlatformNames(platforms.stream().map(Platform::getName).collect(Collectors.toList()));
            &#125;);
            pageInfo.setList(orders);
        &#125;
        <span class="hljs-keyword">return</span> pageInfo;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">严格遵守CQE</h2>
<p>CQE即Command、Query、Event。接收前端创建订单请求使用Command，接收前端分页查询请求使用Query，消费事件（非领域事件）则使用Event。</p>
<p>除Event外，所有写请求都应该使用Command接收参数，而所有查询都应该使用Query接收参数，只在参数只有一个ID的查询情况下，可省略Query。</p>
<p>在查询分离情况下，Query是可直接传递到DAO的（接口层->应用层->DAO)。因此使用Query封装查询条件能够提高方法的复用，当添加查询条件时，无需给方法加多一个参数。</p>
<h2 data-id="heading-3">严格遵守层级依赖</h2>
<p>上层只能依赖下层，下层不能依赖上层。</p>
<p>以经典四层架构来理解更容易，四层架构指基础设施层、领域层、应用层、接口层。</p>
<p>在一次创建订单的操作中，用于接收前端请求参数的CreateOrderCommand属于应用层的类，虽然我们在Controller(接口层)可直接使用CreateOrderCommand，但这属于上层依赖下层，并且不是领域层，也并未暴露聚合根内部结构，因此是允许的。</p>
<p>如果反过来，直接将CreateOrderCommand对象传递给聚合根，那就构成下层依赖上层了，因此这是不允许的。
CreateOrderCommand必须在应用层拆解为创建订单所需要的值对象，或者实体对象，再调用订单工厂创建订单，然后交给资源库持久化订单聚合根。</p>
<h2 data-id="heading-4">建议聚合根ID由代码生成而不是依赖数据库</h2>
<p>因为我们需要在创建聚合根时就知道聚合根的ID，而不是等到最后调用资源库持久化后才返回聚合根的ID，并层层返回。</p>
<p>当我们需要在创建订单后发送创建订单事件时，需要给事件带上订单的ID，而事件又需要聚合根生产（在聚合根持久化后在应用服务中发布，因为聚合根没有事件发布器），当聚合根自己都还不知道自己的ID时，如何创建领域事件呢？</p>
<p>如果实在需要依赖数据库生成ID，那么就由聚合根提供一个回写ID的方法，但不能给聚合根类所有字段提供set方法，聚合根的内部结构不可泄漏给应用层。</p>
<p>End…</p></div>  
</div>
            