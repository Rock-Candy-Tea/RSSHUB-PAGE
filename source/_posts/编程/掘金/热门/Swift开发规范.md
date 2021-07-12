
---
title: 'Swift开发规范'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=1179'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 08:21:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=1179'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>开发规范的目的是保证统一项目成员的编码风格，并使代码美观，每个公司对于代码的规范也不尽相同，希望该份规范能给大家起到借鉴作用。本文为原创，如需转载请说明原文地址链接。</p>
<h2 data-id="heading-1">命名规约</h2>
<ul>
<li>代码中的命名严禁使用拼音及英文混合的方式，更不允许直接出现中文的方式，最好也不要使用下划线或者美元符号开头；</li>
<li>文件名、class、struct、enum、protocol 命名统一使用 UpperCamelCase 风格；</li>
<li>方法名、参数名、成员变量、局部变量、枚举成员统一使用 lowerCamelCase 风格</li>
<li>全局常量命名使用 k 前缀 + UpperCamelCase 命名；</li>
<li>扩展文件，用“原始类型名＋扩展名”作为扩展文件名，其中原始类型名及扩展名也使用 UpperCamelCase 风格，如<code>UIView+Frame.swift</code>；</li>
<li>工程中文件夹或者 Group 统一使用 UpperCamelCase 风格，一律使用单数形式；</li>
<li>命名中出现缩略词时，缩略词要么全部大写，要么全部小写，以首字母大小写为准，通用缩略词包括 JSON、URL 等；如<code>class IDUtil &#123;&#125;</code>、<code>func idToString() &#123; &#125;</code></li>
<li>不要使用不规范的缩写，如 AbstractClass“缩写”命名成 AbsClass 等，不怕名称长，就怕名称不明确。</li>
<li>文件名如果有复数含义，文件名应使用复数形式，如一些工具类；</li>
</ul>
<h2 data-id="heading-2">修饰规约</h2>
<ul>
<li>能用 let 修饰的时候，不要使用 var；</li>
<li>修饰符顺序按照 注解、访问限制、static、final 顺序；</li>
<li>尽可能利用访问限制修饰符控制类、方法等的访问限制；</li>
<li>写方法时，要考虑这个方法是否会被重载。如果不会，标记为 final，final 会缩短编译时间；</li>
<li>在编写库的时候需要注意修饰符的选用，遵循开闭原则；</li>
</ul>
<h2 data-id="heading-3">格式规约</h2>
<ul>
<li>类、函数左大括号不另起一行，与名称之间留有空格</li>
<li>禁止使用无用分号</li>
<li>代码中的空格出现地点
<ul>
<li>注释符号与注释内容之间有空格</li>
<li>类继承, 参数名和类型之间等, 冒号前面不加空格, 但后面跟空格</li>
<li>任何运算符前后有空格</li>
<li>表示返回值的 -> 两边</li>
<li>参数列表、数组、tuple、字典里的逗号后面有一个空格</li>
</ul>
</li>
<li>方法之间空一行</li>
<li>重载的声明放在一起，按照参数的多少从少到多向下排列</li>
<li>每一行只声明一个变量</li>
<li>如果是一个很长的数字时，建议使用下划线按照语言习惯三位或者四位一组分割连接。</li>
<li>表示单例的静态属性，一般命名为 shared 或者 default</li>
<li>如果是空的 block，直接声明&#123; &#125;，括号之间不需换行</li>
<li>解包时推荐使用原有名字，前提是解包后的名字与解包前的名字在作用域上不会形成冲突</li>
<li>if 后面的 else\else if, 跟着上一个 if\else if 的右括号</li>
<li>switch 中, case 跟 switch 左对齐</li>
<li>每行代码长度应小于 100 个字符，或者阅读时候不应该需要滚动屏幕，在正常范围内可以看到完整代码</li>
<li>实现每个协议时, 在单独的 extension 里来实现</li>
</ul>
<h2 data-id="heading-4">简略规约</h2>
<ul>
<li>Swift 会被结构体按照自身的成员自动生成一个非 public 的初始化方法，如果这个初始化方法刚好适合，不要自己再声明</li>
<li>类及结构体初始化方法不要直接调用.init，直接直接省略，使用()</li>
<li>如果只有一个 get 的计算属性，忽略 get</li>
<li>数据定义时，尽量使用字面量形式进行自动推断，如果上下文不足以推断字面量类型时，需要声明赋值类型</li>
<li>省略默认的访问权限（internal）</li>
<li>过滤, 转换等, 优先使用 filter, map 等高阶函数简化代码，并尽量使用最简写</li>
<li>使用闭包时，尽量使用最简写</li>
<li>使用枚举属性时尽量使用自动推断，进行缩写</li>
<li>无用的代码及时删除</li>
<li>尽量使用各种语法糖</li>
<li>访问实例成员或方法时尽量不要使用 <code>self.</code>，特殊场景除外，如构造函数时</li>
<li>当方法无返回值时，不需添加 void</li>
</ul>
<h2 data-id="heading-5">注释规约</h2>
<ul>
<li>文档注释使用单行注释，即///，不使用多行注释，即/***/。 多行注释用于对某一代码段或者设计进行描述</li>
<li>对于公开的类、方法以及属性等必须加上文档注释，方法需要加上对应的<code>Parameter（s）</code>、<code>Returns</code>、<code>Throws</code> 标签，强烈建议使用<code>⌥ ⌘ /</code>自动生成文档模板</li>
<li>在代码中灵活的使用一些地标注释，如<code>MARK</code>、<code>FIXME</code>、<code>TODO</code>，当同一文件中存在多种类型定义或者多种逻辑时，可以使用<code>Mark</code>进行分组注释</li>
<li>尽量将注释另起一行，而不是放在代码后</li>
</ul>
<h2 data-id="heading-6">其他</h2>
<ul>
<li>不要使用魔法值(即未经定义的常量)；</li>
<li>函数参数最多不得超过 8 个；寄存器数目问题，超过 8 个会影响效率；</li>
<li>图形化的字面量，<code>#colorLiteral(...)</code>, <code>#imageLiteral(...)</code>只能用在 playground 当做自我练习使用，禁止在项目工程中使用</li>
<li>避免强制解包以及强制类型映射，尽量使用<code>if let</code> 或 <code>guard let</code>进行解包，禁止<code>try！</code>形式处理异常，避免使用隐式解包</li>
<li>避免判断语句嵌套层次太深，使用 guard 提前返回</li>
<li>如果 for 循环在函数体中只有一个 if 判断，使用 for where 进行替换</li>
<li>实现每个协议时, 尽量在单独的 extension 里来实现；但需要考虑到协议的方法是否有 override 的可能，定义在 extension 的方法无法被 override，除非加上@objc 方法修改其派发方式</li>
<li>优先创建函数而不是自定义操作符</li>
<li>尽可能少的使用全局命名空间，如常量、变量、方法等</li>
<li>赋值数组、字典时每个元素分别占用一行时，最后一个选项后面也添加逗号；这样未来如果有元素加入会更加方便</li>
<li>布尔类型属性使用 is 作为属性名前缀，返回值为布尔型类型的方法名使用 is 作为方法名作为前缀</li>
<li>类似注解的修饰词单独占一行，如@objc，@discardableResult 等</li>
<li>extension 上不用加任何修饰符，修饰符加在 extension 内的变量或方法上</li>
<li>使用 guard 来提前结束条件，避免形成判断嵌套；</li>
<li>善用字典去减少判断，可将条件与结果分别当做 key 及 value 存入字典中；</li>
<li>封装时善用 assert，方便问题排查；</li>
<li>在闭包中使用 self 时使用捕获列表<code>[weak self]</code>避免循环引用，闭包开始判断 self 的有效性</li>
<li>使用委托和协议时，避免循环引用，定义属性的时候使用 weak 修饰</li>
</ul>
<h2 data-id="heading-7">工具</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frealm%2FSwiftLint" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/realm/SwiftLint" ref="nofollow noopener noreferrer">SwiftLint 工具</a> 提示格式错误</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnicklockwood%2FSwiftFormat" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nicklockwood/SwiftFormat" ref="nofollow noopener noreferrer">SwiftFormat 工具</a> 提示并修复格式错误</p>
<p>两者大部分格式规范都是一致的，少许规范不一致，两个工具之间使用不冲突，可以在项目中共存。我们通过配置文件可以控制启用或者关闭相应的规则，具体使用规则参照对应仓库的 REAMME.md 文件。</p>
<h2 data-id="heading-8">相关规范</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fswift.org%2Fdocumentation%2Fapi-design-guidelines%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://swift.org/documentation/api-design-guidelines/" ref="nofollow noopener noreferrer">Swift 官方 API 设计指南</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgoogle.github.io%2Fswift%2F%23apples-markup-format" target="_blank" rel="nofollow noopener noreferrer" title="https://google.github.io/swift/#apples-markup-format" ref="nofollow noopener noreferrer">google 发布的 Swift 编码规范</a></p>
<hr>
<blockquote>
<p>有一个技术的圈子与一群同道众人非常重要，来我的技术公众号及博客，这里只聊技术干货。</p>
<ul>
<li>微信公众号：<strong>CoderStar</strong></li>
<li>博客：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcoder-star.github.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://coder-star.github.io/" ref="nofollow noopener noreferrer">CoderStar's Blog</a></li>
</ul>
</blockquote></div>  
</div>
            