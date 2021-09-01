
---
title: '一篇走心的iOS代码规范'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=4661'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 16:02:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=4661'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>    关于代码规范的重要性这里不做过多解释，能看到这篇文章说明你已经开始重视代码规范了(<code>代码规范看起来是在限制你的自由和发挥，其实它是在间接的帮助你变得更优秀。</code>)。</p>
<p>    适当的代码规范和标准绝不是消灭代码内容的创造性、优雅性，而是限制过度个性化，以一种普遍认可的统一方式一起做事，进而提高工作效率，降低沟通成本。代码的字里行间流淌着的是软件和程序员的血液，质量的提升是尽可能少踩坑、杜绝踩重复的坑，切实提升系统稳定性，码出质量(<code>摘抄自《阿里巴巴Java代码规范》</code>)。</p>
<p>    根据约束力度，暂时把规范约定为2个等级，分别是 <strong>[必须]</strong> 和 <strong>[建议]</strong>。</p>
<h3 data-id="heading-1">(一)命名规范</h3>
<hr>
<h4 data-id="heading-2">1. 通用命名规范</h4>
<pre><code class="copyable">Tips:
所有的命名都应该遵循3个基本原则，即“清晰性”、“一致性”、“不要自我指涉”。
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p><strong>[必须]</strong> 清晰性：好的命名应该是能自我描述的。</p>
<pre><code class="copyable">正例:
removeObject:、[string stringByReplacingOccurrencesOfString:@"1" withString:@"2"]
反例:
remove:(不清楚，要删除什么？)、string.replace("1", "2")(是将"1"替换成"2"还是将"2"替换成"1"？是将第1个"1"替换成"2"还是将所有的"1"都替换成"2")
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 一致性：命名应该和上下文乃至全局保持一致性，相同类型或者具有相同作用的变量的命名方式应该相同或类似。</p>
<pre><code class="copyable">正例:
NSDictionary、NSArray、NSSet这几个集合类都是用count来表示数量而不是一个用count其它的用amount或其他单词，这体现了命名的一致性。

@property (readonly) NSUInteger count;

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 禁止自我指涉：命名不要自我指涉。通知、掩码常量等除外(通常指那些可以进行按位运算的枚举值)。</p>
<pre><code class="copyable">正例:
NSString
反例:
NSStringObject
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 杜绝过度缩写，严禁自创缩写(例如把button缩写为btn)；国际通用缩写名称除外(例如ATM、GPS)。</p>
<pre><code class="copyable">Tips:
你明白这个缩写的意思不代表其他人也一定会明白，你的代码可能会被任何人阅读，而阅读的人来自不同的地方接受不同的教育不同的文化，所有建议一般不要乱使用缩写，只使用那些国际通用缩写。如果为了缩写创建一个缩写对照表只会增加代码阅读复杂度。
正例:
destinationSelection、setBackgroundColor
反例:
destSel、setBgColor
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 杜绝无意义的拼音，国际通用名称或者地名人名除外(例如alibaba、taobao、hangzhou)。</p>
<pre><code class="copyable">反例:
DaZhePromotion(打折)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 命名要尽可能的清晰并简洁，如果两者不能兼得，则以清晰为主。</p>
<pre><code class="copyable">正例:
insertObject:atIndex:
反例:
insert:at:(不清晰，插入什么？at代表什么?)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 代码和注释中都要避免使用任何语言的种族歧视性词语。</p>
<pre><code class="copyable">正例:
secondary
反例:
slave
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 类名、协议名、函数名、常量名、枚举名等一些全局命名需要添加前缀，前缀需要大于2个字符且全部大写。</p>
<pre><code class="copyable">Tips: 系统保留任意两个字符作为前缀的使用权，
包括但不限于NS、UI、CG、CF、CA、WK、MK、CI、NC；前缀若等于2个字符可以考虑添加_。
正例:
ZT_LoginViewController
反例:
ZTLoginViewController
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 类名、协议名、函数名、常量名、枚举名等一些全局命名遵循首字母大写的驼峰命名方式，首个单词是HTTP这种特殊词除外。</p>
</li>
<li>
<p><strong>[必须]</strong> 方法名、属性名等一些非全局命名遵循首字母小写的驼峰命名方式命名，首个单词是HTTP这种特殊词除外。</p>
</li>
<li>
<p><strong>[必须]</strong> 成员变量需要以_开头。</p>
<pre><code class="copyable">正例:
NSString *_nameString;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 在给常量或变量命名时，尽量将表示类型的名词放在词尾，以提升辨识度。</p>
<pre><code class="copyable">正例:
nameLabel、nameString
反例:
name(name是字符串还是什么?)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 如果模块、接口、类、方法使用了模式，在命名时尽量体现出具体模式。</p>
<pre><code class="copyable">正例:
OrderFactory、LoginProxy
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 局部临时变量命名可以加上标识符作为前缀。</p>
<pre><code class="copyable">正例:
t_label、t_string(t在这里表示temp)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-3">2. 类命名规范</h4>
<ul>
<li>
<p><strong>[必须]</strong> 类名命名风格由"前缀+类的名称+类的类型"3个部分组成，前缀必须大于2个字符且全部大写(如果等于2个字符可以添加_)；类的名称遵循首字母大写驼峰式命名，类的名称要能表达出该类的功能；类的类型必须使用全称，严禁使用缩写(例如vc代替viewController，cell代替TableViewCell)，命名方式和名称命名一样首字母大写。</p>
<pre><code class="copyable">正例:
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>WXYZ_LoginViewControler
WXYZ_表示前缀，Login表示该类跟登录相关，ViewController表示该类是一个视图控制器而不是View。
```</p>
<h4 data-id="heading-4">3. 方法命名规范</h4>
<ul>
<li>
<p><strong>[必须]</strong> 所有方法名称禁止以new开始。</p>
</li>
<li>
<p><strong>[必须]</strong> 所有方法名称禁止使用_开始。</p>
<pre><code class="copyable">Tips: 系统会使用_开头命名一些系统私有方法
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 内部私有方法需要增加前缀，前缀需要保持唯一性(例如p_)。</p>
<pre><code class="copyable">Tips: 给私有方法加前缀有2个好处: 
1. 增加辨识度，提高代码可读性。
2. 避免自己的方法无意间覆盖了系统/框架同名的私有方法。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 如果方法返回接收者的某个属性值，那么请直接使用属性名作为方法名。</p>
<pre><code class="copyable">正例:
- (CGSize)cellSize;
反例:
- (CGSize)getCellSize;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 如果方法间接返回一个或多个值，那么请用"getXXX"命名，这种命名只适用于返回多个数据项的情况。</p>
<pre><code class="copyable">正例:
- (void)getCachedResponseForDataTask:(NSURLSessionDataTask *)dataTask 
                   completionHandler:(void (^) (NSCachedURLResponse * __nullable cachedResponse))completionHandler;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 方法的每个参数前都必须添加关键字。</p>
<pre><code class="copyable">正例:
- (void)sendAction:(SEL)aSelector toObject:(id)anObject forAllCells:(BOOL)flag;
反例:
- (void)sendAction:(SEL)aSelector :(id)anObject :(BOOL)flag;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 参数之前的单词尽量能描述参数的意义。</p>
<pre><code class="copyable">正例:
- (id)viewWithTag:(NSInteger)aTag;
反例:
- (id)taggedView:(int)aTag;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 请不要使用“and”连接接收者属性，尽管and读起来还算顺口，但随着你创建的方法参数的增加，这将会带来一系列的问题。</p>
<pre><code class="copyable">正例:
- (int)runModalForDirectory:(NSString *)path file:(NSString *) name types:(NSArray *)fileTypes;
反例:
- (int)runModalForDirectory:(NSString *)path andFile:(NSString *)name andTypes:(NSArray *)fileTypes;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 如果方法描述了两个独立的动作，则可以使用"and"连接起来。</p>
<pre><code class="copyable">正例:
- (BOOL)openFile:(NSString *)fullPath withApplication:(NSString *)appName andDeactivate:(BOOL)flag;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-5">4. Protocol命名规范</h4>
<ul>
<li>
<p><strong>[必须]</strong> Protocol中的方法命名以触发消息的对象名开头，省略类名前缀并首字母小写，如果它没有关联任何类则可以忽略这个规则。</p>
<pre><code class="copyable">正例:
- (BOOL)tableView:(NSTableView *)tableView shouldSelectRow:(int)row;
- (BOOL)application:(NSApplication *)sender openFile:(NSString *)filename;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 除非Protocol方法只有一个参数，否则冒号需紧跟在类名后面。</p>
<pre><code class="copyable">正例:
- (BOOL)tableView:(NSTableView *)tableView shouldSelectRow:(int)row;
- (BOOL)applicationOpenUntitledFile:(NSApplication *)sender;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-6">5. Category命名规范</h4>
<ul>
<li>
<p><strong>[必须]</strong> 分类命名也要和类命名一样添加前缀。</p>
<pre><code class="copyable">正例:
UIView (YYAdd)
反例:
UIView (Add)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 分类中声明的方法名都要加上前缀。</p>
</li>
<li>
<p><strong>[建议]</strong> Category中尽量不要声明属性，能挪尽量挪到主类中声明。</p>
<pre><code class="copyable">Tips: 尽管从技术上来讲可以在分类中声明属性，但是这么做需要格外小心，
因为它很容易出现内存上或其他一些问题，而且一旦出现问题很难排查。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 如果一个类比较复杂，那么建议使用分类组织代码(可以参考系统的UIView)。</p>
</li>
</ul>
<h4 data-id="heading-7">6. Notification命名规范</h4>
<ul>
<li>
<p><strong>[必须]</strong> Notification的命名风格由"类名前缀" + "通知事件名称" + "Notification"3个部分组成。</p>
<pre><code class="copyable">正例:
UIApplicationDidBecomeActiveNotification
UIApplication表示该通知属于谁，DidBecomeActive表示该通知的作用，Notification表示它是一个通知。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 如果一个类声明了delegate属性，通常情况下，这个类的delegate对象应该可以通过实现的delegate方法收到大部分通知消息。</p>
<pre><code class="copyable">Tips: 
例如applicationDidBecomeActive:代理方法和NSApplicationDidBecomeActiveNotification通知(这其实也符合命名规范的基本原则"一致性")。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-8">7. 常量命名规范</h4>
<ul>
<li>
<p><strong>[必须]</strong> 如果常量局限于某"编译单元"之内，通常在前面加小写字母k作为前缀，若常量在全局可见，通常以类名作为前缀，然后采用首字母大写的驼峰式命令风格。</p>
<pre><code class="copyable">正例:
// 局部可见
const CGFloat kAnimationDuration = 2.0;
// 全局可见
const CGFloat UIActivityIndicatorViewAnimationDuration = 2.0;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-9">8. Exception命名规范</h4>
<ul>
<li><strong>[必须]</strong> 命令规范和Notification一样，把后缀改为"Exception"即可。</li>
</ul>
<h4 data-id="heading-10">9. 文件命名规范</h4>
<ul>
<li>
<p><strong>[必须]</strong> 文件名全部小写。</p>
</li>
<li>
<p><strong>[必须]</strong> 采用_连接单词。</p>
</li>
<li>
<p><strong>[必须]</strong> 命名的风格："模块_属性描述"，可根据项目适当增加描述。</p>
<pre><code class="copyable">正例:
public_back@2x.png
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-11">(二)编码规范</h3>
<hr>
<h4 data-id="heading-12">1. 通用编码规范</h4>
<ul>
<li>
<p><strong>[必须]</strong> 如果有使用到CF(Core Foundation)等框架时，或者是在iOS10以下系统使用通知和KVO时，切记在dealloc方法中释放对象以及移除通知和监听。</p>
</li>
<li>
<p><strong>[必须]</strong> 在dealloc方法内禁止将self传递出去，如果self被retain，到下个runloop周期再释放则会多次释放导致crash。</p>
<pre><code class="copyable">反例:
- (void)dealloc &#123;
    [self unsafeMethod:self];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 禁止使用过时的方法或类，应该及时去了解和使用新方法或类。</p>
<pre><code class="copyable">Tips:
对于过时的方法或类，大都是因为其自身有一些缺陷或BUG才会不建议使用，使用新方法时建议了解一下为什么废弃掉旧方法/类。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 对剪切板的读取操作必须放在子线程中进行，因为用户可能在Mac上复制大量数据然后通过iCloud同步到iPhone上。</p>
</li>
<li>
<p><strong>[必须]</strong> if、else、for、while、case等后面必须要有&#123;&#125;，除非后面是简单的return类型语句，例如<code>if (xxx) return;</code>。</p>
</li>
<li>
<p><strong>[必须]</strong> 当方法可能会提前return时，需要要注意对象的释放问题，避免内存泄漏。</p>
<pre><code class="copyable">反例:
CFArrayRef arrayRef = (__bridge CFArrayRef)array;

if (x == YES) return;
 
CFRelease(arrayRef);

以上代码如果x等于YES的话那么arrayRef对象就会内存泄漏。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 当使用@try处理异常时，需要要注意对象的释放问题，避免内存泄漏。</p>
<pre><code class="copyable">反例:
@try &#123;
CFArrayRef arrayRef = (__bridge CFArrayRef)array;
    
do some thing……

CFRelease(arrayRef);
        
&#125; @catch (NSException *exception) &#123;
    
&#125;

以上代码如果do some thing……出现异常的话那么arrayRef就会出现内存泄漏。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 声明常量请使用const类型声明，禁止使用#define宏定义。</p>
<pre><code class="copyable">Tips: 
宏定义声明常量的缺点:
1. 宏定义只是简单的替换，缺少编译检查，运行期可能会出现溢出或数据错误等问题。
2. 宏定义缺少类型，不方便编写文档用例。
3. 宏定义可能会被不小心替换。
4. 宏定义无法编写注释。

反例:
#define kTime @"10"
    
if (1 == 2) &#123;
#define kTime @"20"
&#125;
    
NSLog(@"time = %@", kTime);

以上代码中的if永远不会执行，但是编译器也会将kTime替换为@"20"
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 写一些公共方法时，请尽量使用内联函数或者全局函数而不是宏定义。</p>
<pre><code class="copyable">Tips:
函数不通过对象调用，所以不会走OC的消息转发流程，效率远高于方法调用；而且函数会有返回值和参数类型以及参数检查，而这些都是宏定义没有的。

正例:
UIKIT_STATIC_INLINE NSString * kNSStringFromInteger(NSInteger a) &#123;
    return [NSString stringWithFormat:@"%zd", a];
&#125;
反例:
#define kNSStringFromInteger(a) [NSString stringWithFormat:@"%zd", a]
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> UITableView使用self-sizing实现不等高cell时，请在tableView:cellForRowAtIndexPath:代理方法中给cell设置数据而不是tableView:willDisplayCell:forRowAtIndexPath:代理方法中设置数据。</p>
</li>
<li>
<p><strong>[必须]</strong> 只在必要的时刻使用懒加载。</p>
<pre><code class="copyable">Tips:
只在以下三种情况下才能使用懒加载:
1. 对象的创建需要依赖其他对象
2. 对象可能被使用，也可能不被使用
3. 对象创建比较消耗性能
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 懒加载方法内应该只执行需要初始化的操作，不应该有其他不必要的逻辑代码。</p>
</li>
<li>
<p><strong>[必须]</strong> 使用一目运算符时左右两边不能有空格。</p>
<pre><code class="copyable">正例:
i++、++i、
反例:
i ++、++ i
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 使用二目、三目运算符时左右两边必须有且仅有一个空格。</p>
<pre><code class="copyable">正例:
1 + 2
反例:
1+2
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 采用4个空格缩进，如果要使用Tab字符，请将1个Tab设置成4个空格。</p>
</li>
<li>
<p><strong>[必须]</strong> 使用NSUserDefaults存储数据时禁止调用synchronize方法，因为系统会在合适的时机将数据保存到本地(即使程序闪退等极端情况)。</p>
</li>
<li>
<p><strong>[必须]</strong> 添加到集合中的对象应该是不可变的，或者在加入之后其哈希码是不可变的。</p>
<pre><code class="copyable">反例:
NSMutableSet *sets = [NSMutableSet set];
NSMutableString *string1 = [NSMutableString stringWithString:@"1"];
[sets addObject:string1];
[sets addObject:@"12"];
    
[string1 appendString:@"2"];

当 [string1 appendString:@"2"] 执行完以后sets对象内会包含2个@"12"。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 必须使用CGRectGet获取Frame的各种值，而不是通过frame.的方式获取。</p>
<pre><code class="copyable">Tips: 
CGRect t_frame = CGRectMake(-10, -10, -10, -10);
当一个view的frame设置成t_frame后，其坐标会隐式的转换为CGRectMake(-20, -20, 10, 10)，因为宽高不可能出现负值；这时通过t_frame.的方式获取的值都是错误的，而CGRectGet会自动帮您处理这些隐式转换。

正例:
CGRectGetWidth(frame)、CGRectGetMinX(frame)、CGRectGetMaxX(frame)
反例:
frame.size.width、frame.origin.x、frame.size.width + frame.origin.x
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 单行字符数限制不超过150个，超出需要换行(空格可以除外)，换行时遵循如下原则:</p>
<pre><code class="copyable">Tips:
1. 第二行相对第一行缩进4个空格，从第三行起不再继续缩进。
2. 运算符与下文一起换行。
3. 方法调用的点符号与下文一起换行。

正例:
- (void)setImageWithURL:(nullable NSURL *)imageURL
            placeholder:(nullable UIImage *)placeholder
                options:(YYWebImageOptions)options
               progress:(nullable YYWebImageProgressBlock)progress
               ransform:(nullable YYWebImageTransformBlock)transform
             completion:(nullable YYWebImageCompletionBlock)completion;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 不可变对象尽量使用copy修饰，如果重写使用copy修饰的set方法，请注意调用copy方法。</p>
</li>
<li>
<p><strong>[建议]</strong> 对于一些体积小并且重要的信息，不要频繁的存储到本地，可以使用NSUserDefaults进行存储。它会在合适的时机存储到本地，这避免了频繁的写入操作，而且在某些极端情况下它也能保证数据存储到本地(例如程序闪退等情况)。</p>
</li>
<li>
<p><strong>[建议]</strong> 在多线程环境下谨慎使用可变集合，必要时候可以采用加锁或GCD的同步线程进行保护，或者在访问可变集合时先将其copy为不可变对象然后再对其访问。</p>
</li>
<li>
<p><strong>[建议]</strong> 头文件中尽量不要声明成员变量而是使用属性代替。</p>
</li>
<li>
<p><strong>[建议]</strong> 头文件中的属性尽量声明为只读，可以在实现文件中再将属性声明为可读可写。</p>
<pre><code class="copyable">正例:
@interface WXYZModel : NSObject

@property (nonatomic, readonly) NSString *name;

@end

@interface WXYZModel ()

@property (nonatomic, strong) NSString *name;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 不要使用一个类去维护多个类的内容，例如一个常量类维护所有的常量类，要按常量功能进行归类，分开维护。</p>
<pre><code class="copyable">Tips: 大而全的类，杂乱无章，使用查找功能才能定位到具体位置，不利于理解也不利于维护。

正例:
缓存相关常量类放在CacheCosts下，系统配置相关常量类放在SystemConfigConsts下。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 如果大括号内为空，则简洁的写成&#123;&#125;就行。</p>
</li>
<li>
<p><strong>[建议]</strong> 没有必要增加多余空格来使上下代码的等号对齐。</p>
<pre><code class="copyable">正例:
int a1 = 1;
long a2 = 3;
NSString *a3 = @"";

反例:
int a1       = 1;
long a2      = 3;
NSString *a3 = @"";
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 少用if else，可以使用 if return 替换，if 嵌套最好不超过5层。</p>
<pre><code class="copyable">正例:
if (x == 1) &#123;
……
return;
&#125;

if (x == 2) &#123;
……
return;
&#125;

反例:
if (x == 1) &#123;
……
&#125; else if (x == 2) &#123;
……
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 尽量避免采用取反逻辑运算符，因为取反逻辑不利于快速理解。</p>
<pre><code class="copyable">正例:
if (array == nil) &#123;
……
&#125;
反例:
if (!array) &#123;
……
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 如果用到了很多协议，必要时可以把协议封装到一个单独的头文件中，这样做不仅可以减小编译时间，还能避免循环引用。</p>
</li>
<li>
<p><strong>[建议]</strong> 使用Switch枚举时尽量将所有枚举类型都列举出来而不使用default，这样下次增加枚举类型时如果Switch没有处理会有警告信息。</p>
</li>
<li>
<p><strong>[建议]</strong> 尽量使用字面量语法创建对象，少用与之等价的方法。</p>
<pre><code class="copyable">Tips:
OC中的NSArray、NSString、NSDictionay、NSNumber都有与之对应的字面量语法: @[]、@""、@&#123;&#125;、@()；使用它们有以下优点:
1. 简单易读，提高代码的可读性和可维护性。
2. 使用字面量创建数组、字典时如果元素里在nil则会抛出异常，而使用arrayWithObjects:这些等价方法创建则会丢失nil后的数据，抛出异常能让你知道这里有问题及时修改防止问题在线上发生。

缺点:
1. 使用字面量创建的对象默认是不可变的，如果要创建可变对象需要进行mutableCopy操作。
2. 不支持子类，如果你创建了一个NSString的子类，@""并不会返回你想要的子类对象。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 头文件中尽量少引用其他头文件，尽量使用@class向前声明，每次引入其他头文件时问问自己是否必须要这样做。</p>
</li>
<li>
<p><strong>[建议]</strong> UI控件建议使用weak修饰而不是strong修饰。</p>
</li>
</ul>
<h4 data-id="heading-13">2. 类编码规范</h4>
<ul>
<li>
<p><strong>[必须]</strong> 如果超类的某个初始化方法不适用于子类，那么子类一定要覆写超类的这个方法并解决该问题或抛出异常。</p>
</li>
<li>
<p><strong>[建议]</strong> 尽量不要使用load类方法，如果必须要使用不能在方法内实现复杂逻辑或堵塞线程。</p>
</li>
<li>
<p><strong>[建议]</strong> 尽量减少继承，类的继承尽量不要超过3层，必要时刻可以考虑用分类、协议来代替继承。</p>
</li>
<li>
<p><strong>[建议]</strong> 把一些稳定的、公共的变量或者方法抽取到父类中。子类尽量只维持父类所不具备的特性和功能。</p>
</li>
</ul>
<h4 data-id="heading-14">3. 方法编码规范</h4>
<ul>
<li>
<p><strong>[必须]</strong> 禁止在init等初始化方法内部、getter、setter、dealloc或其他特殊地方使用.语法访问属性。</p>
<pre><code class="copyable">Tips: 当存在继承关系时使用.语法访问会因为多态关系调用子类的实现方法，而如果这个时候子类还没有初始化好或者已经释放了那么可能会出现一些奇怪的问题。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 方法参数在定义和传入时，逗号后面必须添加一个空格。</p>
<pre><code class="copyable">正例:
method(a1, a2, a3);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 单个方法的行数建议不超过80行，注释、左右大括号、空行、回车等除外。</p>
</li>
<li>
<p><strong>[建议]</strong> 在实现文件内部也尽量使用.语法访问属性而不是使用_直接访问成员变量来保证风格统一。</p>
</li>
</ul>
<h4 data-id="heading-15">4. Block编码规范</h4>
<ul>
<li>
<p><strong>[必须]</strong> 调用Block必须判空处理。</p>
<pre><code class="copyable">Tips: 
对于简单的Block可以使用三目运算进行判空处理，
例如 !self.block ?: self.block();
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 在Block内部使用外部变量时要注意循环引用的问题。</p>
<pre><code class="copyable">Tips: 
1. 不一定在Block内使用self才会循环引用，如下情况也会造成循环引用:
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath &#123;
    WXYZ_TitleTableViewCell *cell = ………
    
    cell.refreshTableViewBlock = ^&#123;
        [tableView reloadData];
    &#125;;
    
    return cell;
&#125;

2. Block内部是否要使用weak需要看Block本身和weak的这个对象是否存在直接或间接的相互引用，若无相互引用则不需要使用weak。

3. 如果Block内部使用了strong修饰了外部的weak变量，那么当使用strong指向成员变量时需要进行判空，否则会崩溃，参考以下代码:
__weak typeof(self) weakSelf = self;
    cell.refreshTableViewBlock = ^&#123;
        __strong typeof(weakSelf) strongSelf = weakSelf;
        if (strongSelf != nil) &#123;
            strongSelf->_name = @"name";
        &#125;
    &#125;;
    
如果把(strongSelf != nil)的判断去掉那么可能会崩溃。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-16">5. 通知编码规范</h4>
<ul>
<li>
<p><strong>[必须]</strong> 在发送通知时，请使用<code>userInfo</code>进行传值，而不是<code>object</code>。</p>
</li>
<li>
<p><strong>[必须]</strong> 通知中心是以同步的方式发送请求的，所以不要在通知方法做一些复杂的计算，特别是当它处于主线程的时候，如果想发送异步通知可以使用<code>NSNotificationQueue</code>。</p>
</li>
<li>
<p><strong>[建议]</strong> 在工程里能不用通知尽量不用通知，通知虽然灵活强大，但是如果滥用会导致工程质量下降，出现问题时也比较难排查。</p>
</li>
</ul>
<h4 data-id="heading-17">6. 注释编码规范</h4>
<ul>
<li>
<p><strong>[必须]</strong> 与其绞尽脑汁写注释，不如想想怎么命名；注释是起辅助作用的，好的命名应该是能自我解释的，如果命名可以解释其作用，并且方法没有任何副作用或者注意事项，那么就不用写注释；注释应该帮助别人更快的理解该方法的使用和注意事项，如果该方法有需要注意的地方一定要在注释中体现出来。</p>
</li>
<li>
<p><strong>[必须]</strong> 当修改了方法实现时需要同步修改注释内容。</p>
</li>
<li>
<p><strong>[必须]</strong> 注释不要写的太冗长，要简单易读容易理解。</p>
</li>
<li>
<p><strong>[必须]</strong> 注释的双斜线和内容之间有且仅有一个空格。</p>
<pre><code class="copyable">正例:
// 这是示例注释，请注意在双斜线后有一个空格
- (void)testFunction;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 对于代码注释需谨慎，代码被注释一般有2种可能，1) 后续会恢复此段代码逻辑； 2) 永久不用；对于第1种情况需添加相应注释，如果没有注释信息难以知晓注释动机，后者建议直接删除。如果有需要可以通过代码仓库查阅历史代码。</p>
</li>
<li>
<p><strong>[必须]</strong> 使用特殊注释标记时，请注明标记人和标记时间，注意及时处理这些标记。</p>
<pre><code class="copyable">正例:
/**
* @brief 简要描述
* @author 标明开发该类模块的作者
*/
// FIXME: 有bug，需要修改
- (void)testFunction;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[建议]</strong> 别给糟糕的代码加注释，重构它。</p>
<pre><code class="copyable">Tips: 注释不能美化糟糕的代码。当企图使用注释前，先考虑是否可以通过调整结构，命名等操作，消除写注释的必要。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-18">(三)工程结构规范</h3>
<hr>
<ul>
<li>
<p><strong>[必须]</strong> 局部使用的常量、静态变量声明在@interface之前。</p>
</li>
<li>
<p><strong>[必须]</strong> @property同一类型的声明放在一块，不同类型的声明用2行空格隔开。</p>
<pre><code class="copyable">正例:
@interface MineViewController ()

@property (nonatomic, weak) UIView *headView;

@property (nonatomic, weak) UITableView *tableView;

我是换行符，请忽略
@property (nonatomic, copy) NSArray *dataSourceArray;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 不同逻辑、不同语义、不同业务的代码之间插入一个空行分隔开以提升可读性。</p>
<pre><code class="copyable">正例:
[self createSubviews];
[self createTableview];

[self netRequest];
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>[必须]</strong> 方法归类</p>
<pre><code class="copyable">#pragma mark - LifeCycle(生命周期相关的代码放在最上面)

- (void)dealloc &#123;&#125;

- (void)viewDidLoad &#123;&#125;

- (void)viewWillAppear:(BOOL)animated &#123;&#125;


#pragma mark - Public(公开方法)

// code...
// 上空一行
// 下空两行


#pragma mark - Private(私有方法)


#pragma mark - Override(需要覆盖父类的方法)


#pragma mark - Notification(通知方法)


#pragma mark - Delegate(Delegate需要实现的方法)


#pragma mark - getter/setter
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-19">结语</h3>
<hr>
<p>这只是一篇关于iOS的代码规范，所以某些需要和服务端需要统一的规范(例如错误码)并没有提到，还有些关于如何编写安全代码方面的规范也只是略微提到，因为关于如何写出更安全的代码应该不属于代码规范层面；欢迎大家提出更好的建议或改进，我也会不断更新完善；最后祝大家码出开心，码出质量。</p>
<h3 data-id="heading-20"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2FinternetWei%2Fimages%2Fraw%2Fmaster%2FuPic%2FiOS%25E4%25BB%25A3%25E7%25A0%2581%25E8%25A7%2584%25E8%258C%2583.md" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/internetWei/images/raw/master/uPic/iOS%E4%BB%A3%E7%A0%81%E8%A7%84%E8%8C%83.md" ref="nofollow noopener noreferrer">下载链接</a></h3>
<hr>
<h3 data-id="heading-21">参考</h3>
<hr>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Flibrary%2Farchive%2Fdocumentation%2FCocoa%2FConceptual%2FCodingGuidelines%2FCodingGuidelines.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CodingGuidelines/CodingGuidelines.html" ref="nofollow noopener noreferrer">Cocoa编码规范</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Falibaba%2FAlibaba-Java-Coding-Guidelines" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/alibaba/Alibaba-Java-Coding-Guidelines" ref="nofollow noopener noreferrer">阿里巴巴Java代码规范</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.douban.com%2Fsubject%2F25829244%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://book.douban.com/subject/25829244/" ref="nofollow noopener noreferrer">Effective Objective-C 2.0  编写高质量iOS与OS X代码的52个有效方法</a></li>
<li>网上其他人发布的有关代码规范的文章</li>
</ol></div>  
</div>
            