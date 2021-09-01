
---
title: 'BeeHive源码解析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/639c88beab2447419ce132f112d4e4f1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 03:48:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/639c88beab2447419ce132f112d4e4f1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前年的时候参与了项目的组件化改造，在系统事件和全局事件分发的场景下，我们使用了BeeHive，这里分析一下BeeHive（欠的历史债）！！！</p>
<p>在解析三方库之前，首先要弄清楚这个是做什么的，该怎么用？</p>
<h3 data-id="heading-0">ViewController/View级解耦</h3>
<h4 data-id="heading-1">使用</h4>
<p>在做组件化之前，我们的项目里各个模块不分彼此的相互调用，渐渐的就发展成下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/639c88beab2447419ce132f112d4e4f1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>BeeHive</code>通过<code>Protocol</code>的方式来解决依赖，正常情况下我们从<code>A</code>页面跳转至<code>B</code>页面，会在<code>A</code>页面里直接引用<code>B</code>页面，如下图左侧的引用关系。而在<code>BeeHive</code>的思想里是把B页面对外公开的方法抽象出接口<code>BServiceProtocol</code>，<code>BViewController</code>来实现这个接口，从而使外界本该依赖BViewController的页面通过引用<code>BServiceProtocol</code>就能达到相同的效果，如下图右侧。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aef1a1ca67fb4bc0a5dcc4d546754089~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>遵循这个思想之后每个<code>Modlue</code>都可以抽出自己的<code>ModuleServiceProtocol</code>，然后将他们统一下沉在<code>ServiceProtocol</code>层中，<code>Modlue</code>之间不直接交互，而是通过<code>ServiceProtocol</code>进行交互，典型的面向接口编程，符合依赖倒置的思想。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e48ac681ee94b23acbc47e648602f24~tplv-k3u1fbpfcp-watermark.image" alt="WeChat734f8e7537ade11285ae2dc9f2c7b22a.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体使用如下：
创建<code>BServiceProtocol</code></p>
<pre><code class="copyable">// BServiceProtocol

@protocol BServiceProtocol <NSObject, BHServiceProtocol>

- (void)setParam:(NSDictionary *)param;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建<code>BViewController</code>实现<code>BServiceProtocol</code></p>
<pre><code class="copyable">@interface BViewController : UIViewController <BServiceProtocol>

@end

@implementation BViewController
- (void)setParam:(NSDictionary *)param &#123;
    // do ...
&#125;
@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>BViewController</code>所在<code>module</code>里注册：</p>
<pre><code class="copyable">[[BeeHive shareInstance] registerService:@protocol(BServiceProtocol) service:[BViewController class]];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>AViewController</code>里就可以直接使用：</p>
<pre><code class="copyable">id <BServiceProtocol> bViewController = [[BeeHive shareInstance] createService:@protocol(BServiceProtocol)];
[bViewController setParam:@&#123;@"name":@"gong"&#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">实现</h4>
<pre><code class="copyable">- (void)registerService:(Protocol *)service implClass:(Class)implClass &#123;
    // 检查入参是否为空
    NSParameterAssert(service != nil);
    NSParameterAssert(implClass != nil);
     // 检查传入的类是否遵循了service协议
    if (![implClass conformsToProtocol:service]) &#123;
        if (self.enableException) &#123;
            @throw [NSException exceptionWithName:NSInternalInconsistencyException reason:[NSString stringWithFormat:@"%@ module does not comply with %@ protocol", NSStringFromClass(implClass), NSStringFromProtocol(service)] userInfo:nil];
        &#125;
        return;
    &#125;
    // 检查是否已经注册了service协议，如果注册过则抛出异常
    if ([self checkValidService:service]) &#123;
        if (self.enableException) &#123;
            @throw [NSException exceptionWithName:NSInternalInconsistencyException reason:[NSString stringWithFormat:@"%@ protocol has been registed", NSStringFromProtocol(service)] userInfo:nil];
        &#125;
        return;
    &#125;
    // 将协议和类都转化成String进行保存。
    NSString *key = NSStringFromProtocol(service);
    NSString *value = NSStringFromClass(implClass);
    if (key.length > 0 && value.length > 0) &#123;
        [self.lock lock];
        [self.allServicesDict addEntriesFromDictionary:@&#123;key:value&#125;];
        [self.lock unlock];
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这块逻辑比较简单，需要注意的是每个协议只能对应一个实现类，这里使用了线程锁来保证线程安全，一般在单例类里保证简单数据的线程安全的场景下，我会使用串行队列去实现。</p>
<pre><code class="copyable">- (id)createService:(Protocol *)service withServiceName:(NSString *)serviceName shouldCache:(BOOL)shouldCache &#123;
    // 检查入参是否为空
    if (!serviceName.length) &#123;
        serviceName = NSStringFromProtocol(service);
    &#125;
    id implInstance = nil;
    // 检查是否已经注册了service协议，如果没有则跑出异常
    if (![self checkValidService:service]) &#123;
        if (self.enableException) &#123;
            @throw [NSException exceptionWithName:NSInternalInconsistencyException reason:[NSString stringWithFormat:@"%@ protocol does not been registed", NSStringFromProtocol(service)] userInfo:nil];
        &#125;
    &#125;
    NSString *serviceStr = serviceName;
    // 如果设置了缓存，则从缓存中读取
    if (shouldCache) &#123;
        id protocolImpl = [[BHContext shareInstance] getServiceInstanceFromServiceName:serviceStr];
        if (protocolImpl) &#123;
            return protocolImpl;
        &#125;
    &#125;
    // 通过service获取Class类
    Class implClass = [self serviceImplClass:service];
    // 如果BViewController实现了singleton方法则将其创建为单例
    if ([[implClass class] respondsToSelector:@selector(singleton)]) &#123;
        if ([[implClass class] singleton]) &#123;
            if ([[implClass class] respondsToSelector:@selector(shareInstance)])
                implInstance = [[implClass class] shareInstance];
            else
                implInstance = [[implClass alloc] init];
            // 如果设置了缓存则将这个实例进行保存
            if (shouldCache) &#123;
                [[BHContext shareInstance] addServiceWithImplInstance:implInstance serviceName:serviceStr];
                return implInstance;
            &#125; else &#123;
                return implInstance;
            &#125;
        &#125;
    &#125;
    return [[implClass alloc] init];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不建议使用三方库的缓存逻辑，最好自己去管理这个生成的实例的生命周期。</p>
<h3 data-id="heading-3">系统事件的分发</h3>
<p>进行组件化之前，<code>application</code>的生命周期事件可以直接供各个业务模块使用，组件化之后，业务模块已经被拆出为独立的<code>pod</code>组件，使用<code>application</code>的生命周期事件是一件挺麻烦的事。<code>BeeHive</code>提供了一个比较方便的系统事件分发和订阅的体系。</p>
<h4 data-id="heading-4">使用</h4>
<p>将<code>main</code>方法里的<code>AppDelegate</code>替换为<code>BHAppDelegate</code></p>
<pre><code class="copyable">int main(int argc, char * argv[]) &#123;
    NSString * appDelegateClassName;
    @autoreleasepool &#123;
        // Setup code that might create autoreleased objects goes here.
        appDelegateClassName = NSStringFromClass([BHAppDelegate class]);
    &#125;
    return UIApplicationMain(argc, argv, nil, appDelegateClassName);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在自己的<code>Pod</code>组件里创建<code>module</code>订阅事件，首先要遵循<code>BHModuleProtocol</code>协议，然后在<code>.m</code>的<code>implementation</code>中添加代码<code>BH_EXPORT_MODULE()</code>，接下来就按自己的需要去订阅相应的事件，下侧我订阅的是闪屏页。</p>
<pre><code class="copyable">@interface GAModule : NSObject <BHModuleProtocol>
@end

@implementation GAModule

BH_EXPORT_MODULE()

- (void)modSplash:(BHContext *)context &#123;
    NSLog(@"modSplash");
&#125;
@end
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">实现</h4>
<p>上面例子创建的<code>GAModule</code>和<code>BeeHive</code>的关系如下图，我们将<code>GAModule</code>通过<code>registerModule</code>注册给<code>BHModuleManager</code>，<code>BHAppDelegate</code>负责接收<code>Application</code>的生命周期消息，当有回调回来时会告诉BHModuleManager触发了某个事件，<code>BHModuleManager</code>会触发我们在<code>GAModule</code>里订阅的消息。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e61ee739d3ab4be7b6bbaa519899a187~tplv-k3u1fbpfcp-watermark.image" alt="751628473646_.pic.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体的操作流程如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72b0b6a3727a47f5948c95335b4847f8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先<code>BHModuleManager</code>会维护一个字典，其<code>key</code>为事件的类型，<code>value</code>为注册该事件的<code>BHModule</code>对象集合，<code>BHModule</code>记录着等级和该<code>Module</code>的类名。外界通过<code>registerDynamicModule</code>进行注册，当相应事件被触发时会调用<code>triggerEvent</code>方法，在获取相应事件的集合后，分别通过<code>performSelector:withObject:</code>方法触发。</p>
<h4 data-id="heading-6"><code>BHAnnotation</code></h4>
<p><code>BHAnnotation</code>中提供了宏的方式供使用者简单的注册。其是在编译阶段，将数据存储在特殊的<code>section</code>中，启动<code>APP</code>时在<code>main</code>函数之前从<code>section</code>中取出之前的数据进行注册。</p>
<h5 data-id="heading-7">存数据</h5>
<pre><code class="copyable">#ifndef BeehiveModSectName
#define BeehiveModSectName "BeehiveMods"
#endif

#define BeeHiveDATA(sectname) __attribute((used, section("__DATA,"#sectname" ")))

#define BeeHiveMod(name) \
class BeeHive; char * k##name##_mod BeeHiveDATA(BeehiveMods) = ""#name"";
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>__attribute((used, section("__DATA,"#sectname" ")))</code>其作用是在编译阶段将作用的函数或数据放入指定名为<code>"BeehiveMods"</code>对应的段中。</p>
<h5 data-id="heading-8">注册取数据的时机</h5>
<pre><code class="copyable">__attribute__((constructor))
void initProphet() &#123;
    _dyld_register_func_for_add_image(dyld_callback);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>constructor</code>修饰后的<code>initProphet</code>函数在<code>+load</code>之后<code>main()</code>函数之前调用。接着使用<code>_dyld_register_func_for_add_image</code>来注册<code>dyld_callback</code>，当dyld链接符号时，会调用<code>dyld_callback</code>，这样做是为了在<code>dyld_callback</code>中获取<code>mach_header</code>。</p>
<h5 data-id="heading-9">取数据并注册服务</h5>
<pre><code class="copyable">NSArray<NSString *>* BHReadConfiguration(char *sectionName,const struct mach_header *mhp);
static void dyld_callback(const struct mach_header *mhp, intptr_t vmaddr_slide) &#123;
    // 获取所有的modName数据
    NSArray *mods = BHReadConfiguration(BeehiveModSectName, mhp);
    for (NSString *modName in mods) &#123;
        Class cls;
        if (modName) &#123;
            cls = NSClassFromString(modName);
            if (cls) &#123;
                // 进行注册
                [[BHModuleManager sharedManager] registerDynamicModule:cls];
            &#125;
        &#125;
    &#125;
    // 获取所有服务的映射
    NSArray<NSString *> *services = BHReadConfiguration(BeehiveServiceSectName,mhp);
    for (NSString *map in services) &#123;
        NSData *jsonData =  [map dataUsingEncoding:NSUTF8StringEncoding];
        NSError *error = nil;
        // 解析存储的json
        id json = [NSJSONSerialization JSONObjectWithData:jsonData options:0 error:&error];
        if (!error) &#123;
            if ([json isKindOfClass:[NSDictionary class]] && [json allKeys].count) &#123;
                NSString *protocol = [json allKeys][0];
                NSString *clsName  = [json allValues][0];
                if (protocol && clsName) &#123;
                    // 注册所有的服务映射
                    [[BHServiceManager sharedManager] registerService:NSProtocolFromString(protocol) implClass:NSClassFromString(clsName)];
                &#125;
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">NSArray<NSString *>* BHReadConfiguration(char *sectionName,const struct mach_header *mhp) &#123;
    NSMutableArray *configs = [NSMutableArray array];
    unsigned long size = 0;
    // 获取指定section的数据
    const struct mach_header_64 *mhp64 = (const struct mach_header_64 *)mhp;
    uintptr_t *memory = (uintptr_t*)getsectiondata(mhp64, SEG_DATA, sectionName, &size);
    unsigned long counter = size/sizeof(void*);
    // 遍历获取存储的数据
    for(int idx = 0; idx < counter; ++idx)&#123;
        char *string = (char*)memory[idx];
        NSString *str = [NSString stringWithUTF8String:string];
        if(!str)continue;
        BHLog(@"config = %@", str);
        if(str) [configs addObject:str];
    &#125;
    return configs;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            