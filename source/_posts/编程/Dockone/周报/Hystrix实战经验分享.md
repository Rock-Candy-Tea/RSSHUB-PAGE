
---
title: 'Hystrix实战经验分享'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/c25ec4eddbaa9667e80ba991346388eb.png'
author: Dockone
comments: false
date: 2021-10-11 07:08:31
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/c25ec4eddbaa9667e80ba991346388eb.png'
---

<div>   
<br><h3>背景</h3>Hystrix是Netlifx开源的一款容错框架，防雪崩利器，具备服务降级，服务熔断，依赖隔离，监控（Hystrix Dashboard）等功能。<br>
<br>尽管说Hystrix官方已不再维护，且有Alibaba Sentinel等新框架选择，但从组件成熟度和应用案例等方面看，其实还是有很多项目在继续使用Hystrix中，本人所参与的项目就是其一。故结合个人的Hystrix实战经验与大家分享交流。<br>
<h3>经验总结</h3><h4>隔离策略的选择</h4>Hystrix提供两种资源隔离策略，线程池和信号量。它们之间的异同点如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/c25ec4eddbaa9667e80ba991346388eb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/c25ec4eddbaa9667e80ba991346388eb.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
当请求的服务网络开销比较大，或者是请求比较耗时，我们最好使用线程隔离策略，这样的策略，可以保证大量的容器（Tomcat）线程可用，不会因服务原因，一直处于阻塞或等待状态，快速失败返回。<br>
<br>而在使用缓存（本地内存缓存更适合该场景，Redis等网络缓存需要评估）时，我们可以使用信号量隔离策略，因为这类服务响应快，不会占用容器线程太长时间，而且也减少了线程切换的一些开销，提高了服务效率。<br>
<br>具体使用哪种策略，需根据业务场景综合评估。一般情况下，推荐使用线程池隔离。<br>
<h4>线程池大小与超时时间设置</h4>在线程池隔离策略下，线程池大小及超时时间的设置至关重要，直接影响着系统服务的响应能力。如线程池大小若设置的太大会造成资源浪费及线程切换等开销；若设置的太小又支撑不了用户请求，造成请求排队。而超时时间设置的太长会出现部分长耗时请求阻塞线程，造成其它正常请求排队等待；若设置的太短又会造成太多正常请求被熔断。<br>
<br>对此Hystrix官方给的建议如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/1cdbe9e92bc1ac5771ad5734689ab439.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/1cdbe9e92bc1ac5771ad5734689ab439.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
即转换为以下计算公式：<br>
<ul><li>线程池大小 = 服务TP99响应时长（单位秒） * 每秒请求量 + 冗余缓冲值</li><li>超时时间（单位毫秒） = 1000（毫秒） / 每秒请求量</li></ul><br>
<br>例如某服务TP99情况下每秒钟会接收30个请求，然后每个请求的响应时长是200ms，按如上公式计算可得：<br>
<br>线程池大小 = 0.2 * 30 + 4（冗余缓冲值）= 10，超时时间 = 300ms<br>
<h4>注解叠加</h4>在实际开发中可能会遇到某外部调用方法有Hystrix注解与其它注解一起使用的情况，例如查询方法加上缓存注解。此时需特别注意注解间的执行顺序，避免出现非预期的结果：<br>
<ul><li><strong>缓存注解未生效</strong>，此时Hystrix注解切面的执行是在最外层，由于Hystrix内部执行是通过ProceedingJoinPoint.getTarget()获取目标对象，使用反射调用的方式直接执行到目标对象方法上，从而造成中间其它注解逻辑丢失。可通过指定注解执行顺序@Order解决保证Hystrix注解执行在最里层。</li><li><strong>因缓存异常造成该查询方法被熔断</strong>，如果Hystrix注解切面的执行是在最外层，此时Hystrix熔断管理的方法逻辑除了第三方服务远程调用，也包括了缓存调用逻辑。如果缓存调用出现异常就会算作整个方法异常，从而引起整个方法被熔断。</li></ul><br>
<br><h4>服务的异常处理</h4>先给大家时间看如下代码，检查是否存在问题：<br>
<pre class="prettyprint">@HystrixCommand(fallbackMethod="queryUserByIdFallback")<br>
public User queryUserById(String userId) &#123;<br>
if(StringUtils.isEmpty(userId)) &#123;<br>
throw new BizException("参数不合法");<br>
&#125;<br>
<br>
Result<User> result;<br>
try &#123;<br>
result = userFacade.queryById(userId);<br>
&#125; catch(Exception e) &#123;<br>
log.error("query user error. id=&#123;&#125;", id, e);<br>
&#125;<br>
<br>
if(result != null && result.isSuccess()) &#123;<br>
return result.getData();<br>
&#125;<br>
<br>
return null;<br>
&#125; <br>
</pre><br>
Hystrix在运行过程中会根据调用请求的成功率或失败率信息来确定每个依赖命令的熔断器是否打开。如果打开，后续的请求都会被拒绝。由此可见，对异常的控制是Hystrix运行效果起很大影响。<br>
<br>再回头看上面的例子，会发现两个异常处理问题：<br>
<ul><li><strong>参数校验不通过时的异常处理</strong>，非法参数校验等非系统调用的异常失败不应该影响熔断逻辑，不应该算作失败统计范围内。对此优化建议是将参数校验放到远程调用封装方法的外面，或者封装成HystrixBadRequestException进行抛出。因为在Hystrix内部逻辑中HystrixBadRequestException异常已默认为不算作失败统计范围内。</li><li><strong>try-catch远程调用的异常处理</strong>，对远程服务的直接调用进行try-catch会把异常直接“吞掉”，会直接造成Hystrix获取不到网络异常等服务不可用异常。建议在catch日志记录处理后将异常再throw出来。</li></ul><br>
<br><h4>fallback方法</h4>Hystrix在依赖服务调用时通过增加fallback方法返回默认值的方式来支持服务优雅降级。但fallback的使用也有很多需要注意的地方，大致总结如下：<br>
<ol><li>fallback方法访问级别、参数等要与对应依赖服务一致，对于需要获取触发fallback的异常实例，可以通过fallback方法增加Throwable类型参数（加到最后一个参数）即可。</li><li>fallback 方法中执行的逻辑尽量轻量，如用本地缓存或静态默认值，避免远程调用。</li><li>如果fallback方法里有远程调用，建议也使用Hystrix包装起来，且保证与主命令线程池的隔离。</li><li>对于写操作的远程调用不建议使用fallback降级，写服务的调用失败可以直接抛出给方法调用侧进行业务判断。</li></ol><br>
<br><h4>groupKey、commandKey、threadPoolKey</h4>在使用Hystrix开发中肯定都见过这三个key，但很多人并不理解这三个key的意义以及对Hystrix的作用，尤其是threadPooKey，故在此总结下：<br>
<br><strong>groupKey</strong><br>
<br>通过group key可以对命令方法进行分组，便于Hystrix数据统计、告警及dashboad展示。一般会根据远程服务的业务类型进行区分，如账户服务定义一个group key，订单服务定义另一个group key。<br>
<br>默认值是@HystrixCommand注解标注的方法所在的类名。<br>
<br><strong>commandKey</strong><br>
<br>具体命令方法的标识名称，常用于对该命令进行动态参数设置。<br>
<br>默认值是@HystrixCommand注解标注的方法名。<br>
<br><strong>threadPoolKey</strong><br>
<br>用于标识命令所归属的线程池，具有相同threadPoolKey的命令使用同一个线程池。<br>
<br>若该key不指定，默认值就是groupKey，即@HystrixCommand注解标注的方法所在的类名。<br>
<br>在实际项目中，我们会建议尽量通过threadPoolKey来指定线程池， 而不是通过groupKey的默认方式划分， 因为会存在某个命令需要跟同组其他命令进行线程隔离的场景，以避免互相影响。<br>
<h4>参数优先级</h4>Hystrix默认提供4个级别的参数值配置方式：<br>
<br><strong>全局默认值（Default Value）</strong><br>
<br>Hystrix自身代码默认值，写死在源码中的值，使用方不配置任何参数情况下生效。<br>
<br>例：execution.isolation.thread.timeoutInMilliseconds超时时间全局默认值是1000，单位毫秒。<br>
<br><strong>动态全局默认参数（Default Property）</strong><br>
<br>此类配置参数可变更全局默认值。<br>
<br>例：通过属性名hystrix.command.default.execution.isolation.thread.timeoutInMilliseconds设置的超时时间值<br>
<br><strong>实例初始值（Instant Value）</strong><br>
<br>熔断器实例初始值，配置此类参数后，不再使用默认值。即写在代码注解中的属性值。<br>
<br>例：@HystrixProperty(name = "execution.isolation.thread.timeoutInMilliseconds", value = "5000")<br>
<br><strong>动态实例参数（Instant Property）</strong><br>
<br>可动态调整一个熔断器实例的参数值。<br>
<br>例：通过属性名hystrix.command.HystrixCommandKey.execution.isolation.thread.timeoutInMilliseconds设置的超时时间值。<br>
<br>优先级关系：动态实例参数（Instance Property） > 实例初始值 > 动态全局默认参数（Default Property） > 全局默认值（Default Value）<br>
<h4>基于配置中心实现参数动态配置</h4>Hystrix默认使用Archaius实现动态设置，而Archaius默认会加载classpath下的config.properties文件，可通过在配置文件中加入对应属性key-value实现动态控制Hystrix行为。在分布式项目中使用配置中心进行统一配置管理是标配，因此需要基于配置中心的扩展实现Hystrix参数动态配置功能。<br>
<br>通过跟踪HystrixCommand的创建，发现Hystrix最终通过HystrixDynamicProperties实现类根据参数属性名获取值，而Hystrix本身提供了HystrixDynamicProperties类的扩展机制，见HystrixPlugins类367行代码，可知Hystrix提供四种扩展方法：<br>
<ol><li>通过系统参数hystrix.plugin.HystrixDynamicProperties.implementation</li><li>基于Java SPI机制</li><li>Archaius动态属性扩展实现类（默认）</li><li>Hystrix内置基于System.getProperty的HystrixDynamicProperties实现</li></ol><br>
<br><strong>基于Java SPI机制</strong><br>
<br>基于SPI机制的扩展实现依赖两个类分别是HystrixDynamicProperties与HystrixDynamicProperty，其中HystrixDynamicProperties类是需要实现的Hystrix动态属性扩展spi接口，提供了多个获取动态属性的方法，接口定义如下：<br>
<pre class="prettyprint">public interface HystrixDynamicProperties &#123;<br>
<br>
/**<br>
 * Requests a property that may or may not actually exist.<br>
 * @param name property name, never <code>null</code><br>
 * @param fallback default value, maybe <code>null</code><br>
 * @return never <code>null</code><br>
 */<br>
public HystrixDynamicProperty<String> getString(String name, String fallback);<br>
/**<br>
 * Requests a property that may or may not actually exist.<br>
 * @param name property name, never <code>null</code><br>
 * @param fallback default value, maybe <code>null</code><br>
 * @return never <code>null</code><br>
 */<br>
public HystrixDynamicProperty<Integer> getInteger(String name, Integer fallback);<br>
/**<br>
 * Requests a property that may or may not actually exist.<br>
 * @param name property name, never <code>null</code><br>
 * @param fallback default value, maybe <code>null</code><br>
 * @return never <code>null</code><br>
 */<br>
public HystrixDynamicProperty<Long> getLong(String name, Long fallback);<br>
/**<br>
 * Requests a property that may or may not actually exist.<br>
 * @param name property name<br>
 * @param fallback default value<br>
 * @return never <code>null</code><br>
 */<br>
public HystrixDynamicProperty<Boolean> getBoolean(String name, Boolean fallback);<br>
&#125; <br>
</pre><br>
而HystrixDynamicProperty类具体表示一个参数属性，且有动态变更的能力，接口定义如下：<br>
<pre class="prettyprint">public interface HystrixDynamicProperty<T> extends HystrixProperty<T>&#123;<br>
<br>
public String getName();<br>
<br>
/**<br>
 * Register a callback to be run if the property is updated.<br>
 * @param callback callback.<br>
 */<br>
public void addCallback(Runnable callback);<br>
<br>
&#125; <br>
</pre><br>
其中addCallback方法是实现属性动态变更的核心所在，如其注释说明的那样，它会在属性变更时注册callback回调方法进行属性动态刷新。而这块动态刷新逻辑是Hystrix内部已实现的，对于我们只需要自定义扩展时将callback保存，然后在配置中心变更时触发对应属性对象的callback方法即可。<br>
<br>实现步骤如下：<br>
<br>1、定义HystrixDynamicProperty实现类<br>
<br>完成动态属性类的自定义实现，包括String/Integer/Long/Boolean四种类型动态属性态实现。<br>
<br>如上面HystrixDynamicProperty类描述中说的那样，需要对callback进行保存，并在在收到配置中心属性变更时触发这些属性的callback方法，来实现属性的动态变更。这块逻辑可以参照观察者模式进行设计实现。<br>
<br>代码如下：<br>
<pre class="prettyprint">private abstract static class CustomDynamicProperty<T> implements HystrixDynamicProperty<T>, PropertyObserver &#123;<br>
    protected final String name;<br>
    protected final T defaultValue;<br>
    protected List<Runnable> callbacks;<br>
<br>
    protected CustomDynamicProperty(String propName, T defaultValue) &#123;<br>
        this.name = propName;<br>
        this.defaultValue = defaultValue;<br>
<br>
        PropertyObserverManager.add(this);<br>
    &#125;<br>
<br>
    @Override<br>
    public String getName() &#123;<br>
        return name;<br>
    &#125;<br>
<br>
    @Override<br>
    public void addCallback(Runnable callback) &#123;<br>
        if (callbacks == null)<br>
            callbacks = new ArrayList<>(1);<br>
        this.callbacks.add(callback);<br>
    &#125;<br>
<br>
    @Override<br>
    public String keyName() &#123;<br>
        return name;<br>
    &#125;<br>
<br>
    @Override<br>
    public void update(PropertyItem item) &#123;<br>
        if(getName().equals(item.getName())) &#123;<br>
            for(Runnable r : callbacks) &#123;<br>
                r.run();<br>
            &#125;<br>
        &#125;<br>
    &#125;<br>
&#125;<br>
<br>
private static class StringDynamicProperty extends CustomDynamicProperty<String> &#123;<br>
    protected StringDynamicProperty(String propName, String defaultValue) &#123;<br>
        super(propName, defaultValue);<br>
    &#125;<br>
<br>
    @Override<br>
    public String get() &#123;<br>
        return ConfigManager.getString(name, defaultValue);<br>
    &#125;<br>
&#125;<br>
<br>
private static class IntegerDynamicProperty extends CustomDynamicProperty<Integer> &#123;<br>
    protected IntegerDynamicProperty(String propName, Integer defaultValue) &#123;<br>
        super(propName, defaultValue);<br>
    &#125;<br>
<br>
    @Override<br>
    public Integer get() &#123;<br>
        String configValue =  ConfigManager.get(name);<br>
        if(StringUtils.isNotEmpty(configValue)) &#123;<br>
            return Integer.valueOf(configValue);<br>
        &#125;<br>
        return defaultValue;<br>
    &#125;<br>
&#125;<br>
<br>
private static class LongDynamicProperty extends CustomDynamicProperty<Long> &#123;<br>
    protected LongDynamicProperty(String propName, Long defaultValue) &#123;<br>
        super(propName, defaultValue);<br>
    &#125;<br>
<br>
    @Override<br>
    public Long get() &#123;<br>
        String configValue =  ConfigManager.get(name);<br>
        if(StringUtils.isNotEmpty(configValue)) &#123;<br>
            return Long.valueOf(configValue);<br>
        &#125;<br>
        return defaultValue;<br>
    &#125;<br>
&#125;<br>
<br>
private static class BooleanDynamicProperty extends CustomDynamicProperty<Boolean> &#123;<br>
    protected BooleanDynamicProperty(String propName, Boolean defaultValue) &#123;<br>
        super(propName, defaultValue);<br>
    &#125;<br>
<br>
    @Override<br>
    public Boolean get() &#123;<br>
        String configValue =  ConfigManager.get(name);<br>
        if(StringUtils.isNotEmpty(configValue)) &#123;<br>
            return Boolean.valueOf(configValue);<br>
        &#125;<br>
        return defaultValue;<br>
    &#125;<br>
&#125; <br>
</pre><br>
其中ConfigManager类暂时默认为配置中心配置管理类，提供参数获取与参数监听器等功能。而PropertyObserver类（keyName/update方法属于其定义）、PropertyObserverManager类就是参照观察者模式定义实现的，负责观察者的注册与通知管理，来完成动态属性与配置中心变更通知间的联动。这两个类实现比较简单就不展示描述。<br>
<br>2、定义HystrixDynamicProperties实现类<br>
<br>基于第1步定义的HystrixDynamicProperty扩展类完成HystrixDynamicProperties的自定义。代码如下：<br>
<pre class="prettyprint">public class DemoHystrixDynamicProperties implements HystrixDynamicProperties &#123;<br>
@Override<br>
public HystrixDynamicProperty<String> getString(String name, String fallback) &#123;<br>
    return new StringDynamicProperty(name, fallback);<br>
&#125;<br>
<br>
@Override<br>
public HystrixDynamicProperty<Integer> getInteger(String name, Integer fallback) &#123;<br>
    return new IntegerDynamicProperty(name, fallback);<br>
&#125;<br>
<br>
@Override<br>
public HystrixDynamicProperty<Long> getLong(String name, Long fallback) &#123;<br>
    return new LongDynamicProperty(name, fallback);<br>
&#125;<br>
<br>
@Override<br>
public HystrixDynamicProperty<Boolean> getBoolean(String name, Boolean fallback) &#123;<br>
    return new BooleanDynamicProperty(name, fallback);<br>
&#125;<br>
&#125; <br>
</pre><br>
3、注册SPI实现类<br>
<br>在META-INF/services/添加名为com.netflix.hystrix.strategy.properties.HystrixDynamicProperties的文本文件，内容为第2步HystrixDynamicProperties自定义实现类全路径名。<br>
<br><strong>基于默认Archaius进行扩展</strong><br>
<br>Hystrix默认通过Archaius实现参数动态获取，而Archaius自身也提供自定义的参数获取方式，分别是PolledConfigurationSource接口和AbstractPollingScheduler类，其中PolledConfigurationSource接口表示配置获取源，AbstractPollingScheduler类表示配置定时刷新机制。<br>
<br>实现步骤如下：<br>
<br>1、创建配置获取源：<br>
<pre class="prettyprint">public class CustomCfgConfigurationSource implements PolledConfigurationSource &#123;<br>
private final static String CONFIG_KEY_PREFIX = "hystrix";<br>
<br>
@Override<br>
public PollResult poll(boolean initial, Object checkPoint) throws Exception &#123;<br>
    Map<String, Object> map = load();<br>
    return PollResult.createFull(map);<br>
&#125;<br>
<br>
private Map<String, Object> load() throws Exception&#123;<br>
    Map<String, Object> map = new HashMap<>();<br>
<br>
    Set<String> keys = ConfigManager.keys();<br>
    for(String key : keys) &#123;<br>
        if(key.startsWith(CONFIG_KEY_PREFIX)) &#123;<br>
            map.put(key, ConfigManager.get(key));<br>
        &#125;<br>
    &#125;<br>
<br>
    return map;<br>
&#125;<br>
&#125; <br>
</pre><br>
其实现非常简单，核心实现就是poll方法，遍历配置中心中所有Hystrix开头的配置参数并返回保存。<br>
<br>2、定义配置刷新方式：<br>
<pre class="prettyprint">public class CustomCfgPollingScheduler extends AbstractPollingScheduler &#123;<br>
private final static Logger logger = LoggerFactory.getLogger("CustomCfgPollingScheduler");<br>
<br>
private final static String CONFIG_KEY_PREFIX = "hystrix";<br>
<br>
@Override<br>
public void startPolling(PolledConfigurationSource source, final Configuration config) &#123;<br>
    super.startPolling(source, config);<br>
    //<br>
    ConfigManager.addListener(new ConfigListener() &#123;<br>
        @Override<br>
        public void eventReceived(PropertyItem item, ChangeEventType type) &#123;<br>
            String name = item.getName();<br>
            if(name.startsWith(CONFIG_KEY_PREFIX)) &#123;<br>
                String newValue = item.getValue();<br>
                //新增&修改<br>
                if(ChangeEventType.ITEM_ADDED.equals(type) || ChangeEventType.ITEM_UPDATED.equals(type)) &#123;<br>
                    addOrChangeProperty(name, newValue, config);<br>
                &#125;<br>
                //删除<br>
                else if(ChangeEventType.ITEM_REMOVED.equals(type)) &#123;<br>
                    deleteProperty(name, config);<br>
                &#125;<br>
                else &#123;<br>
                    logger.error("error config change event type &#123;&#125;.", type);<br>
                &#125;<br>
            &#125;<br>
        &#125;<br>
    &#125;);<br>
&#125;<br>
<br>
private void addOrChangeProperty(String name, Object newValue, final Configuration config) &#123;<br>
    if (!config.containsKey(name)) &#123;<br>
        config.addProperty(name, newValue);<br>
    &#125; else &#123;<br>
        Object oldValue = config.getProperty(name);<br>
        if (newValue != null) &#123;<br>
            if (!newValue.equals(oldValue)) &#123;<br>
                config.setProperty(name, newValue);<br>
            &#125;<br>
        &#125; else if (oldValue != null) &#123;<br>
            config.setProperty(name, null);<br>
        &#125;<br>
    &#125;<br>
&#125;<br>
<br>
private void deleteProperty(String key, final Configuration config) &#123;<br>
    if (config.containsKey(key)) &#123;<br>
        config.clearProperty(key);<br>
    &#125;<br>
&#125;<br>
<br>
@Override<br>
protected void schedule(Runnable pollingRunnable) &#123;<br>
    //IGNORE OPERATION<br>
&#125;<br>
<br>
@Override<br>
public void stop() &#123;<br>
    //IGNORE OPERATION<br>
&#125;<br>
&#125; <br>
</pre><br>
AbstractPollingScheduler类默认要求是定义一个定时任务实现定时刷新配置，而其方法schedule和stop方法就是分别对应启动定时任务和结束任务。  <br>
<br>但对应实际项目，通过定时刷新的方式一是不太实时，二是每次都得全量检查配置中心是否有修改，逻辑复杂，所以此处改用 ConfigManager.addListener 增加配置中心监听来实现。<br>
<br>3、定义并初始化自动配置：<br>
<pre class="prettyprint">DynamicConfiguration dynamicConfiguration = new DynamicConfiguration(new CustomCfgConfigurationSource(), new CustomCfgPollingScheduler());<br>
ConfigurationManager.install(dynamicConfiguration);<br>
</pre><br>
最后只需要在容器启动时执行以上初始化脚本即可。<br>
<br>细心的同学可能发现上面步骤中第3步，最终“安装”install到Hystrix配置管理类中的是 DynamicConfiguration类实现，且第2步的定时刷新类也比较鸡肋，就想着能否继续简化上面方案，只需要实现一个自定义的"DynamicConfiguration"就包含配置源获取与监听配置修改功能，实现如下：<br>
<pre class="prettyprint">public class CustomCfgDynamicConfiguration extends ConcurrentMapConfiguration &#123;<br>
private final static Logger logger = LoggerFactory.getLogger("CustomCfgDynamicConfiguration");<br>
<br>
private final static String CONFIG_KEY_PREFIX = "hystrix";<br>
<br>
public CustomCfgDynamicConfiguration() &#123;<br>
    super();<br>
    load();<br>
    initEvent();<br>
&#125;<br>
<br>
/**<br>
 * 从配置中心全量加载Hystrix配置参数信息<br>
 */<br>
private void load() &#123;<br>
    Set<String> keys = ConfigManager.keys();<br>
    for(String key : keys) &#123;<br>
        if(key.startsWith(CONFIG_KEY_PREFIX)) &#123;<br>
            map.put(key, ConfigManager.get(key));<br>
        &#125;<br>
    &#125;<br>
&#125;<br>
<br>
/**<br>
 * 通过配置中心监听事件回调处理，针对Hystrix配置参数变更进行同步<br>
 */<br>
private void initEvent() &#123;<br>
    ConfigManager.addListener(new ConfigListener() &#123;<br>
        @Override<br>
        public void eventReceived(PropertyItem item, ChangeEventType type) &#123;<br>
            String name = item.getName();<br>
            if(name.startsWith(CONFIG_KEY_PREFIX)) &#123;<br>
                String newValue = item.getValue();<br>
                //新增&修改<br>
                if(ChangeEventType.ITEM_ADDED.equals(type) || ChangeEventType.ITEM_UPDATED.equals(type)) &#123;<br>
                    addOrChangeProperty(name, newValue);<br>
                &#125;<br>
                //删除<br>
                else if(ChangeEventType.ITEM_REMOVED.equals(type)) &#123;<br>
                    deleteProperty(name);<br>
                &#125;<br>
                else &#123;<br>
                    logger.error("error config change event type &#123;&#125;.", type);<br>
                &#125;<br>
            &#125;<br>
        &#125;<br>
    &#125;);<br>
&#125;<br>
<br>
/**<br>
 * 新增或修改参数值<br>
 * @param name<br>
 * @param newValue<br>
 */<br>
private void addOrChangeProperty(String name, Object newValue) &#123;<br>
    if (!this.containsKey(name)) &#123;<br>
        this.addProperty(name, newValue);<br>
    &#125; else &#123;<br>
        Object oldValue = this.getProperty(name);<br>
        if (newValue != null) &#123;<br>
            if (!newValue.equals(oldValue)) &#123;<br>
                this.setProperty(name, newValue);<br>
            &#125;<br>
        &#125; else if (oldValue != null) &#123;<br>
            this.setProperty(name, null);<br>
        &#125;<br>
    &#125;<br>
&#125;<br>
<br>
/**<br>
 * 删除参数值<br>
 * @param key<br>
 */<br>
private void deleteProperty(String key) &#123;<br>
    if (this.containsKey(key)) &#123;<br>
        this.clearProperty(key);<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
最后通过ConfigurationManager.install(new CustomCfgDynamicConfiguration());“安装”该实现即可。<br><br>
<h3>写在最后</h3>笔者结合项目实战对Hystrix使用进行总结分享，有关于隔离策略、线程池设置、参数优先级等知识点讲解，也有关于注解叠加、异常处理、参数动态配置等具体问题解决方案，希望对大家有所帮助。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/jA_hvMgt7VmkHWjavAax_Q" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/jA_hvMgt7VmkHWjavAax_Q</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            