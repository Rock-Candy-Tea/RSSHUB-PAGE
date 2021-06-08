
---
title: '知识点：iOS 中的协议—@protocol'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=2429'
author: 掘金
comments: false
date: Thu, 13 May 2021 01:13:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=2429'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1. 关于Protocol</h3>
<p>在使用OC开发iOS程序的过程中经常会用到Protocol，定义一个Protocol的语法格式如下：</p>
<pre><code class="copyable">@protocol HumanProtocol <NSObject>

@required
- (void)name;
- (void)age;

//@optional
// ...

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>iOS中协议的概念似于java中的接口interface，就是一堆方法的声明，但没有实现。一个类可以遵循一个或多个协议，任何类只要遵循了协议就相当于拥有了这个协议中所有的方法声明。Protocol可以定义在一个类的头文件上部，并直接应用在该类中（如作为delegate功能使用时），Protocol也可单独定义到一个类中，作为多个不同类来遵循并实现的interface。</p>
<pre><code class="copyable">//// .h文件
#import <Foundation/Foundation.h>

@protocol HumanProtocol <NSObject>

@required
- (void)name;
- (void)age;

//@optional
// ...

@end

@interface Tom : NSObject

@property (nonatomic, copy) id<HumanProtocol> delegate;

@end


//// .m文件
#import "Tom.h"

@interface Tom : NSObject <HumanProtocol>

@end

@implementation Tom

// 实现定义的方法
- (void)name &#123;
&#125;
- (void)age &#123;
&#125;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<p>或，将HumanProtocol写成一个独立的类文件，然后导入：</p>
<pre><code class="copyable">#import <Foundation/Foundation.h>
#import "HumanProtocol.h"

@interface Tom : NSObject <HumanProtocol>

@property (nonatomic, copy) id<HumanProtocol> delegate;

@end

@implementation Tom

// 调用协议变量，或实现协议方法

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2. 使用示例</h3>
<p>是一个基协议，每个新协议都需要遵循。@protocol是定义一个协议的注解，其中，@required表示这个方法必须被实现，@optional表示这个方法不一定要被实现。</p>
<p><strong>应用场景：</strong>
一个人需要一个Blog（Blog内容可以不同），这个Blog必须有通用的学习、分享等功能。则需求如下：</p>
<p>1、需要创建一个人和Blog；
2、需要创建一个Protocol来描述这些功能；
3、人拥有的Blog要实现这些功能；
4、Blog需要遵循这个Protocol且实现它。</p>
<pre><code class="copyable">#import <Foundation/Foundation.h>

@protocol BlogProtocol <NSObject>
- (void)study;
- (void)share;
@end

----------------------------

#import <Foundation/Foundation.h>
#import "BlogProtocol.h"

@class Blog;
@interface Person : NSObject
//拥有的Blog要实现Protocol的功能
@property (nonatomic,strong) Blog<BlogProtocol> *blog;
@end

----------------------------

#import <Foundation/Foundation.h>
#import "BlogProtocol.h"

@interface Blog : NSObject<BlogProtocol>
@end

#import "Blog.h"
@implementation Blog
- (void)study &#123;
    NSLog(@"%s",__func__);
&#125;
- (void)share &#123;
    NSLog(@"%s",__func__);
&#125;
@end

----------------------------

Person *p = [[Person alloc] init];
Blog *blog = [[Blog alloc] init];
// 此处会判断Blog是否符合协议的Blog，否则报警告
p.blog = blog;

//判断Blog是否有实现协议内容
if ([p.blog respondsToSelector:@selector(study)]) &#123;
    [p.blog study];
&#125;
if ([p.blog respondsToSelector:@selector(share)]) &#123;
    [p.blog share];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3. 需要注意的几个点</h3>
<p><strong>协议与继承的区别</strong>：继承之后默认就有实现，而协议只要声明没有实现；相同类型的类可以使用继承，但是不同类型的类只能使用协议；协议可以用于存储方法声明，可以将多个类中共有的方法抽取出来，以后让这些类遵守协议即可</p>
<p><strong>协议与 Category 的区别</strong>：category是针对类进行扩展，而且该类必须有里面的所有成员，协议不同可以选择性实现；category是针对一个具体的类实现，其他类没有，协议允许任何类使用并实现；Category由本身实现，不允许其他类重写，协议只定义方法，无具体实现任何类允许自己实现；category被单继承的特性所限制，协议则没有继承限制。</p>
<pre><code class="copyable">//// Protocol类
@protocol SportProtocol <NSObject>
@property (nonatomic,copy) NSString *sportType;
- (void)playFootball;
- (void)playBasketball;
- (void)run;
@end

//// 实现类：Person
#import <Foundation/Foundation.h>
#import "SportProtocol.h"

@interface Person : NSObject<SportProtocol>
@end

#import "Person.h"
@implementation Person
@synthesize sportType=_sportType;

- (void)readSportType&#123;
   NSLog(@"%@",_sportType);
&#125;
@end

// Person *p =[[Person alloc]init];
// p.sportType = @"sport";
// [p readSportType];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面方法中用到了@synthesize sportType=_sportType，sportType 属性为 _sportType 成员变量合成访问器方法。</p>
<pre><code class="copyable">//// 继承类：Student
#import "Person.h"
@interface Student : Person
@end

// Student *stu = [[Student alloc]init];
// [stu playBasketball];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个类可以遵守多个protocol，protocol又可以遵守其他protocol:</p>
<pre><code class="copyable">//// 遵守多个protocol
#import <Foundation/Foundation.h>
#import "SportProtocol.h"
#import "StudyProtocol.h"

@interface Person : NSObject<SportProtocol, StudyProtocol>
@end

//// protocol遵守其他protocol
#import <Foundation/Foundation.h>
#import "BaseProtocol.h"

@protocol StudyProtocol <BaseProtocol>
- (void)studyEnglish;
- (void)studyChinese;
@end
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><em><strong>protocol中既可以声明方法，也可以声明属性；一个类可以遵守多个protocol；protocol又可以遵守其他protocol；父类遵守了某个类的protocol，那么子类也会自动遵守这个Protocol。</strong></em></p>
</blockquote></div>  
</div>
            