
---
title: 'vivo全球商城时光机 - 大型促销活动保障利器'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd064a67bb2549f9bf3a293b7463a37f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 19:20:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd064a67bb2549f9bf3a293b7463a37f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、背景</h1>
<p>官网商城在双11、双12等大促期间运营同学会精心设计许多给到用户福利的促销活动，当促销活动花样越来越多后就会涉及到很多的运营配置工作(如指定活动有效期，指定活动启停状态，指定活动参与商品等等）。</p>
<p>如果因为某些原因导致其中部分配置未按预期配置，等到大促那一刻才发现配置没有正确配置，这样大概率会流失不少订单，同样也可能会出现错配优惠导致一些本不该享受的优惠也被用户享受到，可能会给商城带来比较大的损失，因此为了尽量减小前面这些情况的发生的概率，我们就想能不能提供一种能力，让运营同学在重要的电商大促正式开始前，提前去校验所有期待的优惠是否配置正确。</p>
<h1 data-id="heading-1">二、构思</h1>
<p>想让运营同学能去校验所配的大促优惠是否正常，同时又希望不会增加多余的额外工作，如何做到呢？</p>
<p>考虑到电商业务的特殊性，所配置的各种大促优惠最终主要都会体现在优惠后的价格上，因此我们考虑从这个角度去实现。</p>
<p>在电商的核心链路上，主要有商详页、购物车、确认订单、提交订单这几个核心场景，那么只需在这几个场景中实现提前看到优惠后的价格即可判断大促优惠是否配置正确。</p>
<p>那现在的关键问题是如何做到**「提前」<strong>看到呢？在前序的促销系列文章我们介绍了计价中心的建设，计价中心统一收口了所有的优惠价的计算能力，因此我们只要让计价中心能提供</strong>「提前」**的能力即可。</p>
<p>计价中心计算优惠价正常只会实时计算当前时间商品能够享受的各种优惠，并将最终优惠价告诉上游业务方，所以我们能让计价中心能够计算「未来某个时间点」的优惠价即可，而计价中心在计算优惠价时，依赖的一个关键信息是**「当前时间」<strong>，因此我们只要将所谓的</strong>「当前时间」<strong>进行</strong>「篡改」**变成未来的某个时间点，实现我们所谓的穿越的目的。</p>
<p>还有一个极为重要的点需要关注，也是这个穿越能力的大前提，就是不能影响线上正常交易，即不能让正常的普通用户也**「提前」**看到未来的优惠价。</p>
<p>因此如何做到既让运营体验又不影响正常用户呢？我们考虑采用白名单机制，只针对已登录且用户id在白名单中的用户才能进行所谓的穿越体验。</p>
<p>在确定大体思路后，还有一些问题需要确认：</p>
<h4 data-id="heading-2">对于穿越的完整体验是否只需要商城购物流程？</h4>
<p>如果需体验大促期间整个官网商城的所有氛围，可能涉及改动的点较为多，比如大促宣传活动页面、专属聚合类商品页面，简化版的只关注整个购物下单流程。</p>
<h4 data-id="heading-3">整个穿越过程是否需要真的要真实创建订单？</h4>
<p>由于穿越时光后，用户的下单时间和确认订单的时间是一致的，因此确认订单页的所有优惠及最终的价格是真正的所见即所得，无需真实下单即可获知所有优惠活动信息</p>
<p>所以在提交订单的时候建议直接阻断并提醒用户“您当前处于时空穿越，请回到现实中再下单哦”，并不作真正的创建订单，也就不会作后续许多写资源的连锁操作，同时这种情况下也会减少很多不必要的改动点。</p>
<h4 data-id="heading-4">对于穿越过程中领取的用户特殊券是否需要作特殊标识？</h4>
<p>a)穿越过程中领取的券，如果作了特殊标识，那么退出时光机后，到了优惠券真实可用期后，应建议不作使用，防止占用普通用户资源，同时这种情况下也不建议增加优惠券已发券数量。</p>
<p>b)穿越过程中领取的券，不作特殊标识，那么退出时光机后使用该券与其他正常领取的券并无差别，这种情况算是占用了普通用户资源，那么相应的也建议增加优惠券已发券数量上。</p>
<p>a方案需要优惠券系统作相关的适配改动，但线上真实资源无任何污染或占用；b方案无需作任何改动，但会侵占极少量真实资源，如果运营方觉得问题不大建议采用b方案，从项目角度成本最小。</p>
<h1 data-id="heading-5">三、实现</h1>
<h2 data-id="heading-6">3.1 核心流程图</h2>
<p>根据前述的构思方案，得出如下商城穿越核心购物流程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd064a67bb2549f9bf3a293b7463a37f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">3.2 改造重点</h2>
<p>从上述流程图中可以看出改造的重点：</p>
<ul>
<li>
<p>白名单信息的维护</p>
</li>
<li>
<p>获取「当前时间」</p>
</li>
</ul>
<h3 data-id="heading-8">3.2.1 白名单信息维护</h3>
<p>为方便后续穿越用户时间信息共享，我们将此信息（openId: travelTime）存储在配置中心中，并提供相应的管理台方便设置穿越用户及穿越时间点。</p>
<h3 data-id="heading-9">3.2.2 获取「当前时间」</h3>
<p>整个上下游关联系统可能都会需要获取**「当前时间」<strong>，而获取</strong>「当前时间」<strong>需要能获取到配置的白名单信息以及当前用户信息。显然为了各个业务系统能尽可能减少代码变动，获取</strong>「当前时间」<strong>适合做到一个公共模块中，各个业务系统依赖这个公共模块自动具备能获取所期待的</strong>「当前时间」**。</p>
<p>因此集成了时光机模块后的整个业务系统链路关系如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ec33c6c07df47ca9b01045e8adc5b9b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">3.2.3 时光机模块</h3>
<p>从前述内容，我们可以得出时光机模块（vivo-xxx-time-travel）中需要包含的主要能力：</p>
<ul>
<li>
<p>a )穿越用户白名单信息</p>
</li>
<li>
<p>b )获取「当前时间」</p>
</li>
<li>
<p>c )读取、设置上下文openId</p>
</li>
</ul>
<p>其中a、b的实现都比较简单，只需正常接入公司的配置中心，并根据指定openId获取**「当前时间」<strong>即可，比较麻烦一点的是获取</strong>「当前时间」**时的这个用户openId信息。</p>
<p>之前的各个业务系统间的接口调用可能是不需要用户openId信息的，但现在穿越用户是指定白名单用户的，所以必须要将入口链路检测到的用户openId信息一路向下传递到下游的各个业务系统中。</p>
<p>**方案一：**各个业务系统间接口调用耦合openId信息，需要各个业务系统全部都改造一遍，显然这个方案比较初级原始也对各业务方非常不友好，非常不建议采用。方案二：由于我们后端各个业务系统间都使用dubbo进行接口调用，因此我们可以利用dubbo基于spi插件机制的定制业务过滤器将openId当作附加接口调用时的附加信息进行透传。（如果是其他接口调用方式的，也建议采用类似原理的处理方式）</p>
<p>下面我们就看下时光机模块中一些核心的代码实现：（当前业务系统作为消费方时执行的过滤器）</p>
<p><strong>当前业务系统作为消费方时执行的过滤器</strong></p>
<pre><code class="copyable">/**
 * 当前业务系统作为消费方时执行的过滤器
 */
@Activate(group = Constants.CONSUMER)
public class BizConsumerFilter implements Filter &#123;
 
    @Override
    public Result invoke(Invoker<?> invoker, Invocation invocation) throws RpcException &#123;
        if (invocation instanceof RpcInvocation) &#123;
            String openId = invocation.getAttachment("tc_xxx_travel_openId");
            if (openId == null && TimeTravelUtil.getContextOpenId() != null) &#123;
                // 作为消费方在发起调用前，如果缺失openId,则设置上下文的openId
                ((RpcInvocation) invocation).setAttachment(openIdAttachmentKey, TimeTravelUtil.getContextOpenId());
            &#125;
        &#125;
        return invoker.invoke(invocation);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>当前业务系统作为服务提供方执行的过滤器；</strong></p>
<pre><code class="copyable">/**
 * 当前业务系统作为服务提供方时执行的过滤器
 */
@Activate(group = Constants.PROVIDER)
public class BizProviderFilter implements Filter &#123;
 
    @Override
    public Result invoke(Invoker<?> invoker, Invocation invocation) throws RpcException &#123;
        if (invocation instanceof RpcInvocation) &#123;
            String openId = invocation.getAttachment("tc_xxx_travel_openId");
            if (openId != null) &#123;// 作为下游服务提供方，获取上游系统设置的上下文openId
                TimeTravelUtil.setContextOpenId(openId);
            &#125;
        &#125;
        try &#123;
            return invoker.invoke(invocation);
        &#125; finally &#123;
            TimeTravelUtil.removeContextOpenId();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>穿越时间获取工具类；</strong></p>
<pre><code class="copyable">/**
 * 穿越时间获取工具类
 */
public final class TimeTravelUtil &#123;
 
    private static final ThreadLocal<TimeTravelInfo> currentUserTimeTravelInfoThreadLocal = new ThreadLocal<>();
    private static final ThreadLocal<String> contextOpenId = new ThreadLocal<>();
 
    public static void setContextOpenId(String openId) &#123;
        contextOpenId.set(openId);
        setUserTravelInfoIfExists(openId);
    &#125;
 
    public static String getContextOpenId() &#123;
        return contextOpenId.get();
    &#125;
 
    public static void removeContextOpenId() &#123;
        contextOpenId.remove();
        removeUserTimeTravelInfo();
    &#125;
 
    /**
     * 设置当前上下文用户穿越信息，如果存在的话
     * @param openId
     */
    public static void setUserTravelInfoIfExists(String openId) &#123;
        // TimeTravellersConfig 会接入配置中心，承载所有白名单穿越用户信息配置，并将每一个穿越用户信息转换为TimeTravelInfo
        TimeTravelInfo userTimeTravelInfo = TimeTravellersConfig.getUserTimeTravelInfo(openId);
        if (userTimeTravelInfo.isInTravel()) &#123;
            currentUserTimeTravelInfoThreadLocal.set(userTimeTravelInfo);
        &#125;
    &#125;
 
    /**
     * 移除当前上下文用户穿越信息
     */
    public static void removeUserTimeTravelInfo() &#123;
        currentUserTimeTravelInfoThreadLocal.remove();
    &#125;
 
    /**
     * 当前链路上下文是否处于穿越中
     * @return
     */
    public static boolean isInTimeTravel() &#123;
        return currentUserTimeTravelInfoThreadLocal.get() != null;
    &#125;
 
    /**
     * 获取「当前」时间，单位：毫秒。
     * 若当前是穿越中，则返回设置的穿越时间,否则返回实际系统时间
     * @return
     */
    public static long getNow() &#123;
        TimeTravelInfo travelInfo = currentUserTimeTravelInfoThreadLocal.get();
        return travelInfo != null ? travelInfo.getTravelTime() : System.currentTimeMillis();
    &#125;
 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>用户穿越信息</strong></p>
<pre><code class="copyable">/**
 * 用户穿越信息
 */
public class TimeTravelInfo &#123;
    /**
     * 当前是否处于穿越中
     */
    private boolean isInTravel = false;
 
    /**
     * 当前穿越时间点，仅在isInTravel=true时有效
     */
    private Long travelTime;
 
    public boolean isInTravel() &#123;
        return isInTravel;
    &#125;
 
    public void setInTravel(boolean inTravel) &#123;
        isInTravel = inTravel;
    &#125;
 
    public Long getTravelTime() &#123;
        return travelTime;
    &#125;
 
    public void setTravelTime(Long travelTime) &#123;
        this.travelTime = travelTime;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在业务系统依赖这个vivo-xxx-time-travel模块后，凡是需要获取当前时间的地方将原来的System.currentTimeMillis()改为TimeTravelUtil.getNow()即可。</p>
<h2 data-id="heading-11">3.4 问题</h2>
<p>在时光机能力建设过程中碰到一个比较重要的问题，就是上下文传递openId信息时，会出现跨线程传递丢失问题。</p>
<p>如果底层是Java线程池直接实现异步调用，那通过对线程池相关拦截可以实现上下文复制拷贝传递，我们内部的全链路系统已经通过相关代理技术对线程上下文信息已作了相关处理。如果使用Hystrix实现异步调用，可以看下笔者另一篇专门介绍的文章《Hystrix中如何解决ThreadLocal信息丢失》 。</p>
<h1 data-id="heading-12">四、最后</h1>
<p>本文介绍的时光机相关能力主要应用在官网商城，但并不局限于电商场景，时光机模块在设计的时候就没有与某个具体业务耦合，因此对于其他一些业务场景也可以适用或者有一些借鉴意义。</p>
<p>另外本文中电商场景中关注的是优惠价格是否正常，基本涉及到的是读操作，如果有些场景需要穿越后进行完整的业务功能操作，如进行实际下单，那么就会涉及到一些写操作，此时可以借助影子库的相关能力去完成完整的穿越操作之旅。</p>
<blockquote>
<p>作者：vivo官网商城开发团队-Wei Fuping</p>
</blockquote></div>  
</div>
            