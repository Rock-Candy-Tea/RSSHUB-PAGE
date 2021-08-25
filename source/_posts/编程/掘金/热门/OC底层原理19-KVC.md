
---
title: 'OC底层原理19-KVC'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b69a14ef523a49619878d30d48b56d65~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 00:22:55 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b69a14ef523a49619878d30d48b56d65~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“<strong>这是我参与8月更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong>”</p>
<h1 data-id="heading-0">前言</h1>
<p><code>KVC</code>又称键值编码 <code>（Key-Value-Coding）</code>，在iOS开发中是一个比较常见的技术点，相信很多开发人员都使用过<code>KVC</code>，其主要的两个方法就是如下两个，分别对应设置值和取值：</p>
<ul>
<li><code>(void)setValue:(nullable id)value forKey:(NSString *)key;</code></li>
<li><code>(nullable id)valueForKey:(NSString *)key;</code></li>
</ul>
<h1 data-id="heading-1">一.<code>KVC</code>简单应用</h1>
<pre><code class="hljs language-js copyable" lang="js">    LGPerson *person = [[LGPerson alloc] init];

    <span class="hljs-comment">// 一般setter 方法</span>

    person.name      = @<span class="hljs-string">"LG_Cooci"</span>; <span class="hljs-comment">// setter -- llvm</span>

    person.age       = <span class="hljs-number">18</span>;

    person->myName   = @<span class="hljs-string">"cooci"</span>;

    NSLog(@<span class="hljs-string">"%@ - %d - %@"</span>,person.name,person.age,person->myName);

   

    <span class="hljs-comment">// 1:Key-Value Coding (KVC) : 基本类型 - 看底层原理</span>

    <span class="hljs-comment">// 非正式协议 - 间接访问</span>

    [person setValue:@<span class="hljs-string">"KC"</span> forKey:@<span class="hljs-string">"name"</span>];

    

    <span class="hljs-comment">// 2:KVC - 集合类型</span>

    person.array = @[@<span class="hljs-string">"1"</span>,@<span class="hljs-string">"2"</span>,@<span class="hljs-string">"3"</span>];

    <span class="hljs-comment">// 修改数组</span>

    <span class="hljs-comment">// person.array[0] = @"100";</span>

    <span class="hljs-comment">// 第一种:搞一个新的数组 - KVC 赋值就OK</span>

    NSArray *array = [person valueForKey:@<span class="hljs-string">"array"</span>];

    array = @[@<span class="hljs-string">"100"</span>,@<span class="hljs-string">"2"</span>,@<span class="hljs-string">"3"</span>];

    [person setValue:array forKey:@<span class="hljs-string">"array"</span>];

    NSLog(@<span class="hljs-string">"%@"</span>,[person valueForKey:@<span class="hljs-string">"array"</span>]);

    <span class="hljs-comment">// 第二种</span>

    NSMutableArray *mArray = [person mutableArrayValueForKey:@<span class="hljs-string">"array"</span>];

    mArray[<span class="hljs-number">0</span>] = @<span class="hljs-string">"200"</span>;

    NSLog(@<span class="hljs-string">"%@"</span>,[person valueForKey:@<span class="hljs-string">"array"</span>]);
    <span class="hljs-comment">// 3:KVC - 集合操作符</span>
    <span class="hljs-comment">// 4:KVC - 访问非对象属性 - 面试可能问到</span>
    <span class="hljs-comment">// 结构体</span>

    ThreeFloats floats = &#123;<span class="hljs-number">1.</span>,<span class="hljs-number">2.</span>,<span class="hljs-number">3.</span>&#125;;

    NSValue *value     = [NSValue valueWithBytes:&floats objCType: **@encode**(ThreeFloats)];

    [person setValue:value forKey:@<span class="hljs-string">"threeFloats"</span>];

    NSValue *value1    = [person valueForKey:@<span class="hljs-string">"threeFloats"</span>];

    NSLog(@<span class="hljs-string">"%@"</span>,value1);


    ThreeFloats th;

    [value1 getValue:&th];

    NSLog(@<span class="hljs-string">"%f-%f-%f"</span>,th.x,th.y,th.z);

    <span class="hljs-comment">// 5:KVC - 层层访问 - keyPath</span>

    LGStudent *student = [LGStudent alloc];

    student.subject    = @<span class="hljs-string">"大师班"</span>;

    person.student     = student;

    [person setValue:@<span class="hljs-string">"Swift"</span> forKeyPath:@<span class="hljs-string">"student.subject"</span>];

    NSLog(@<span class="hljs-string">"%@"</span>,[person valueForKeyPath:@<span class="hljs-string">"student.subject"</span>]);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">#pragma mark **- array取值**

- (**<span class="hljs-keyword">void</span>**)arrayDemo&#123;

    LGStudent *p = [LGStudent <span class="hljs-keyword">new</span>];

    p.penArr = [NSMutableArray arrayWithObjects:@<span class="hljs-string">"pen0"</span>, @<span class="hljs-string">"pen1"</span>, @<span class="hljs-string">"pen2"</span>, @<span class="hljs-string">"pen3"</span>, **nil**];

    NSArray *arr = [p valueForKey:@<span class="hljs-string">"pens"</span>]; <span class="hljs-comment">// 动态成员变量</span>

    NSLog(@<span class="hljs-string">"pens = %@"</span>, arr);

    <span class="hljs-comment">//NSLog(@"%@",arr[0]);</span>

    NSLog(@<span class="hljs-string">"%d"</span>,[arr containsObject:@<span class="hljs-string">"pen9"</span>]);

    <span class="hljs-comment">// 遍历</span>

    NSEnumerator *enumerator = [arr objectEnumerator];

    NSString* str = **nil**;

    **<span class="hljs-keyword">while</span>** (str = [enumerator nextObject]) &#123;

        NSLog(@<span class="hljs-string">"%@"</span>, str);

    &#125;

&#125;

#pragma mark **- 字典操作**
- (**<span class="hljs-keyword">void</span>**)dictionaryTest&#123;

    

    NSDictionary* dict = @&#123;

                           @<span class="hljs-string">"name"</span>:@<span class="hljs-string">"Cooci"</span>,

                           @<span class="hljs-string">"nick"</span>:@<span class="hljs-string">"KC"</span>,

                           @<span class="hljs-string">"subject"</span>:@<span class="hljs-string">"iOS"</span>,

                           @<span class="hljs-string">"age"</span>:@<span class="hljs-number">18</span>,

                           @<span class="hljs-string">"length"</span>:@<span class="hljs-number">180</span>

                           &#125;;

    LGStudent *p = [[LGStudent alloc] init];

    <span class="hljs-comment">// 字典转模型</span>

    [p setValuesForKeysWithDictionary:dict];

    NSLog(@<span class="hljs-string">"%@"</span>,p);

    <span class="hljs-comment">// 键数组转模型到字典</span>

    NSArray *array = @[@<span class="hljs-string">"name"</span>,@<span class="hljs-string">"age"</span>];

    NSDictionary *dic = [p dictionaryWithValuesForKeys:array];

    NSLog(@<span class="hljs-string">"%@"</span>,dic);

&#125;
#pragma mark **- KVC消息传递**

- (**<span class="hljs-keyword">void</span>**)arrayMessagePass&#123;

    NSArray *array = @[@<span class="hljs-string">"Hank"</span>,@<span class="hljs-string">"Cooci"</span>,@<span class="hljs-string">"Kody"</span>,@<span class="hljs-string">"CC"</span>];

    NSArray *lenStr= [array valueForKeyPath:@<span class="hljs-string">"length"</span>];

    NSLog(@<span class="hljs-string">"%@"</span>,lenStr);<span class="hljs-comment">// 消息从array传递给了string</span>

    NSArray *lowStr= [array valueForKeyPath:@<span class="hljs-string">"lowercaseString"</span>];

    NSLog(@<span class="hljs-string">"%@"</span>,lowStr);

&#125;
#pragma mark **- 聚合操作符**

<span class="hljs-comment">// @avg、@count、@max、@min、@sum</span>

- (**<span class="hljs-keyword">void</span>**)aggregationOperator&#123;

    NSMutableArray *personArray = [NSMutableArray array];

    **<span class="hljs-keyword">for</span>** (**int** i = <span class="hljs-number">0</span>; i < <span class="hljs-number">6</span>; i++) &#123;

        LGStudent *p = [LGStudent <span class="hljs-keyword">new</span>];

        NSDictionary* dict = @&#123;

                               @<span class="hljs-string">"name"</span>:@<span class="hljs-string">"Tom"</span>,

                               @<span class="hljs-string">"age"</span>:@(<span class="hljs-number">18</span>+i),

                               @<span class="hljs-string">"nick"</span>:@<span class="hljs-string">"Cat"</span>,

                               @<span class="hljs-string">"length"</span>:@(<span class="hljs-number">175</span> + <span class="hljs-number">2</span>*arc4random_uniform(<span class="hljs-number">6</span>)),

                               &#125;;

        [p setValuesForKeysWithDictionary:dict];

        [personArray addObject:p];

    &#125;

    NSLog(@<span class="hljs-string">"%@"</span>, [personArray valueForKey:@<span class="hljs-string">"length"</span>]);

    

    <span class="hljs-comment">/// 平均身高</span>

    **float** avg = [[personArray valueForKeyPath:@<span class="hljs-string">"@avg.length"</span>] floatValue];

    NSLog(@<span class="hljs-string">"%f"</span>, avg);

    

    **int** count = [[personArray valueForKeyPath:@<span class="hljs-string">"@count.length"</span>] intValue];

    NSLog(@<span class="hljs-string">"%d"</span>, count);

    

    **int** sum = [[personArray valueForKeyPath:@<span class="hljs-string">"@sum.length"</span>] intValue];

    NSLog(@<span class="hljs-string">"%d"</span>, sum);

    

    **int** max = [[personArray valueForKeyPath:@<span class="hljs-string">"@max.length"</span>] intValue];

    NSLog(@<span class="hljs-string">"%d"</span>, max);

    

    **int** min = [[personArray valueForKeyPath:@<span class="hljs-string">"@min.length"</span>] intValue];

    NSLog(@<span class="hljs-string">"%d"</span>, min);

&#125;

<span class="hljs-comment">// 数组操作符 @distinctUnionOfObjects @unionOfObjects</span>

- (**<span class="hljs-keyword">void</span>**)arrayOperator&#123;

    NSMutableArray *personArray = [NSMutableArray array];

    **<span class="hljs-keyword">for</span>** (**int** i = <span class="hljs-number">0</span>; i < <span class="hljs-number">6</span>; i++) &#123;

        LGStudent *p = [LGStudent <span class="hljs-keyword">new</span>];

        NSDictionary* dict = @&#123;

                               @<span class="hljs-string">"name"</span>:@<span class="hljs-string">"Tom"</span>,

                               @<span class="hljs-string">"age"</span>:@(<span class="hljs-number">18</span>+i),

                               @<span class="hljs-string">"nick"</span>:@<span class="hljs-string">"Cat"</span>,

                               @<span class="hljs-string">"length"</span>:@(<span class="hljs-number">175</span> + <span class="hljs-number">2</span>*arc4random_uniform(<span class="hljs-number">6</span>)),

                               &#125;;

        [p setValuesForKeysWithDictionary:dict];

        [personArray addObject:p];

    &#125;

    NSLog(@<span class="hljs-string">"%@"</span>, [personArray valueForKey:@<span class="hljs-string">"length"</span>]);

    <span class="hljs-comment">// 返回操作对象指定属性的集合</span>

    NSArray* arr1 = [personArray valueForKeyPath:@<span class="hljs-string">"@unionOfObjects.length"</span>];

    NSLog(@<span class="hljs-string">"arr1 = %@"</span>, arr1);

    <span class="hljs-comment">// 返回操作对象指定属性的集合 -- 去重</span>

    NSArray* arr2 = [personArray valueForKeyPath:@<span class="hljs-string">"@distinctUnionOfObjects.length"</span>];

    NSLog(@<span class="hljs-string">"arr2 = %@"</span>, arr2);

    

&#125;
<span class="hljs-comment">// 嵌套集合(array&set)操作 @distinctUnionOfArrays @unionOfArrays @distinctUnionOfSets</span>

- (**<span class="hljs-keyword">void</span>**)arrayNesting&#123;

    

    NSMutableArray *personArray1 = [NSMutableArray array];

    **<span class="hljs-keyword">for</span>** (**int** i = <span class="hljs-number">0</span>; i < <span class="hljs-number">6</span>; i++) &#123;

        LGStudent *student = [LGStudent <span class="hljs-keyword">new</span>];

        NSDictionary* dict = @&#123;

                               @<span class="hljs-string">"name"</span>:@<span class="hljs-string">"Tom"</span>,

                               @<span class="hljs-string">"age"</span>:@(<span class="hljs-number">18</span>+i),

                               @<span class="hljs-string">"nick"</span>:@<span class="hljs-string">"Cat"</span>,

                               @<span class="hljs-string">"length"</span>:@(<span class="hljs-number">175</span> + <span class="hljs-number">2</span>*arc4random_uniform(<span class="hljs-number">6</span>)),

                               &#125;;

        [student setValuesForKeysWithDictionary:dict];

        [personArray1 addObject:student];

    &#125;

    

    NSMutableArray *personArray2 = [NSMutableArray array];

    **<span class="hljs-keyword">for</span>** (**int** i = <span class="hljs-number">0</span>; i < <span class="hljs-number">6</span>; i++) &#123;

        LGPerson *person = [LGPerson <span class="hljs-keyword">new</span>];

        NSDictionary* dict = @&#123;

                               @<span class="hljs-string">"name"</span>:@<span class="hljs-string">"Tom"</span>,

                               @<span class="hljs-string">"age"</span>:@(<span class="hljs-number">18</span>+i),

                               @<span class="hljs-string">"nick"</span>:@<span class="hljs-string">"Cat"</span>,

                               @<span class="hljs-string">"length"</span>:@(<span class="hljs-number">175</span> + <span class="hljs-number">2</span>*arc4random_uniform(<span class="hljs-number">6</span>)),

                               &#125;;

        [person setValuesForKeysWithDictionary:dict];

        [personArray2 addObject:person];

    &#125;

    

    <span class="hljs-comment">// 嵌套数组</span>

    NSArray* nestArr = @[personArray1, personArray2];

    

    NSArray* arr = [nestArr valueForKeyPath:@<span class="hljs-string">"@distinctUnionOfArrays.length"</span>];

    NSLog(@<span class="hljs-string">"arr = %@"</span>, arr);

    

    NSArray* arr1 = [nestArr valueForKeyPath:@<span class="hljs-string">"@unionOfArrays.length"</span>];

    NSLog(@<span class="hljs-string">"arr1 = %@"</span>, arr1);

&#125;
- (**<span class="hljs-keyword">void</span>**)setNesting&#123;

    

    NSMutableSet *personSet1 = [NSMutableSet set];

    **<span class="hljs-keyword">for</span>** (**int** i = <span class="hljs-number">0</span>; i < <span class="hljs-number">6</span>; i++) &#123;

        LGStudent *person = [LGStudent <span class="hljs-keyword">new</span>];

        NSDictionary* dict = @&#123;

                               @<span class="hljs-string">"name"</span>:@<span class="hljs-string">"Tom"</span>,

                               @<span class="hljs-string">"age"</span>:@(<span class="hljs-number">18</span>+i),

                               @<span class="hljs-string">"nick"</span>:@<span class="hljs-string">"Cat"</span>,

                               @<span class="hljs-string">"length"</span>:@(<span class="hljs-number">175</span> + <span class="hljs-number">2</span>*arc4random_uniform(<span class="hljs-number">6</span>)),

                               &#125;;

        [person setValuesForKeysWithDictionary:dict];

        [personSet1 addObject:person];

    &#125;

    NSLog(@<span class="hljs-string">"personSet1 = %@"</span>, [personSet1 valueForKey:@<span class="hljs-string">"length"</span>]);

    

    NSMutableSet *personSet2 = [NSMutableSet set];

    **<span class="hljs-keyword">for</span>** (**int** i = <span class="hljs-number">0</span>; i < <span class="hljs-number">6</span>; i++) &#123;

        LGPerson *person = [LGPerson <span class="hljs-keyword">new</span>];

        NSDictionary* dict = @&#123;

                               @<span class="hljs-string">"name"</span>:@<span class="hljs-string">"Tom"</span>,

                               @<span class="hljs-string">"age"</span>:@(<span class="hljs-number">18</span>+i),

                               @<span class="hljs-string">"nick"</span>:@<span class="hljs-string">"Cat"</span>,

                               @<span class="hljs-string">"length"</span>:@(<span class="hljs-number">175</span> + <span class="hljs-number">2</span>*arc4random_uniform(<span class="hljs-number">6</span>)),

                               &#125;;

        [person setValuesForKeysWithDictionary:dict];

        [personSet2 addObject:person];

    &#125;

    NSLog(@<span class="hljs-string">"personSet2 = %@"</span>, [personSet2 valueForKey:@<span class="hljs-string">"length"</span>]);
    <span class="hljs-comment">// 嵌套set</span>
    NSSet* nestSet = [NSSet setWithObjects:personSet1, personSet2, **nil**];
    <span class="hljs-comment">// 交集</span>
    NSArray* arr1 = [nestSet valueForKeyPath:@<span class="hljs-string">"@distinctUnionOfSets.length"</span>];
    NSLog(@<span class="hljs-string">"arr1 = %@"</span>, arr1);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">二.<code>KVC</code>简介-苹果官方文档重要</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fios%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/ios/" ref="nofollow noopener noreferrer">苹果开发iOS地址</a></p>
<h1 data-id="heading-3">三.苹果官方文档解释<code>KVC</code></h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Flibrary%2Farchive%2Fdocumentation%2FCocoa%2FConceptual%2FKeyValueCoding%2Findex.html%23%2F%2Fapple_ref%2Fdoc%2Fuid%2F10000107i" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i" ref="nofollow noopener noreferrer">KVC地址</a></p>
<h1 data-id="heading-4">四.<code>KVC</code>设值和取值过程</h1>
<p><code>KVC</code>设置</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b69a14ef523a49619878d30d48b56d65~tplv-k3u1fbpfcp-watermark.image" alt="Xnip2021-08-08_15-00-28.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>KVC</code>设置值的过程</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3cc089cf0ea4aed89a6625afad69245~tplv-k3u1fbpfcp-watermark.image" alt="Xnip2021-08-08_15-06-56.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行的优先顺序按照苹果官方文档所示<code>set<Key>:</code>-><code> _set<key>:</code></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d01c683c044448aa6e4659df7dafbe8~tplv-k3u1fbpfcp-watermark.image" alt="Xnip2021-08-08_15-10-03.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当 <code>accessInstanceVariablesDirectly</code> 设置为<code>YES</code>时 获取实例变量的顺序为顺序查找名称为<code>_<key></code>-><code>_is<Key></code>-><code><key></code>-><code>is<Key></code></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3cb4f281931487da1b31129eec63303~tplv-k3u1fbpfcp-watermark.image" alt="Xnip2021-08-08_15-15-32.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bcdd1e8ccb44203ae902357d5d89621~tplv-k3u1fbpfcp-watermark.image" alt="Xnip2021-08-08_15-15-58.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>_<key></code>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/155aa12c74604e819f72cd6c32787fad~tplv-k3u1fbpfcp-watermark.image" alt="Xnip2021-08-08_15-16-45.jpg" loading="lazy" referrerpolicy="no-referrer">
<code>_is<Key></code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9913fc5e6c4542a3866269867f491fbb~tplv-k3u1fbpfcp-watermark.image" alt="Xnip2021-08-08_15-17-37.jpg" loading="lazy" referrerpolicy="no-referrer">
<code><key></code></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bce746346dd94af3989ab57a5300c787~tplv-k3u1fbpfcp-watermark.image" alt="Xnip2021-08-08_15-18-03.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>is<Key></code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6347c84c7d1467b84f477ddd4cb8746~tplv-k3u1fbpfcp-watermark.image" alt="Xnip2021-08-08_15-18-29.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>按照官方文档说 如果没有以上都没有 就会进入下面这个方法
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/862dbbcddbd54d9987f19641ea154217~tplv-k3u1fbpfcp-watermark.image" alt="Xnip2021-08-08_15-24-00.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>KVC</code>取值的过程</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90db784aee244ff7aa69aa58e9a7a1e5~tplv-k3u1fbpfcp-watermark.image" alt="Xnip2021-08-08_15-26-47.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行顺序按照官方文档 <code>get<Key></code>-><code><key></code>-><code>is<Key></code>-><code>_<key></code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7db8df330e4b44bb9560632ce92ccb08~tplv-k3u1fbpfcp-watermark.image" alt="Xnip2021-08-08_15-31-10.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果以上都没有 按照<code>_<key></code>-><code>_is<Key></code>-><code><key></code>-><code>is<Key></code>取</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ab88e4304db48b39ed2597d0ffe07ef~tplv-k3u1fbpfcp-watermark.image" alt="Xnip2021-08-08_15-40-37.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>细节当我们注释掉<code>_name</code> 打印<code>name</code> 显示的是<code>_isName</code> 顺序问题</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24eb0a01c216444db3616d7fb05c294c~tplv-k3u1fbpfcp-watermark.image" alt="Xnip2021-08-08_15-42-40.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果都没有的话 就会调用 <code>valueForUndefinedKey:</code>这个方法</p>
<h1 data-id="heading-5">五.<code>KVC</code>自定义实现</h1>
<pre><code class="hljs language-js copyable" lang="js">- (**<span class="hljs-keyword">void</span>**)lg_setValue:(**nullable** **id**)value forKey:(NSString *)key&#123;

    <span class="hljs-comment">// KVC 自定义</span>

    <span class="hljs-comment">// 1: 判断什么 key</span>

    **<span class="hljs-keyword">if</span>** (key == **nil** || key.length == <span class="hljs-number">0</span>) &#123;

        **<span class="hljs-keyword">return</span>**;

    &#125;
    <span class="hljs-comment">// 2: setter set<Key>: or _set<Key>,</span>

    <span class="hljs-comment">// key 要大写</span>

    NSString *Key = key.capitalizedString;

    <span class="hljs-comment">// 拼接方法</span>

    NSString *setKey = [NSString stringWithFormat:@<span class="hljs-string">"set%@:"</span>,Key];

    NSString *_setKey = [NSString stringWithFormat:@<span class="hljs-string">"_set%@:"</span>,Key];

    NSString *setIsKey = [NSString stringWithFormat:@<span class="hljs-string">"setIs%@:"</span>,Key];

    

    **<span class="hljs-keyword">if</span>** ([**self** lg_performSelectorWithMethodName:setKey value:value]) &#123;

        NSLog(@<span class="hljs-string">"*********%@**********"</span>,setKey);

        **<span class="hljs-keyword">return</span>**;

    &#125;**<span class="hljs-keyword">else</span>** **<span class="hljs-keyword">if</span>** ([**self** lg_performSelectorWithMethodName:_setKey value:value]) &#123;

        NSLog(@<span class="hljs-string">"*********%@**********"</span>,_setKey);

        **<span class="hljs-keyword">return</span>**;

    &#125;**<span class="hljs-keyword">else</span>** **<span class="hljs-keyword">if</span>** ([**self** lg_performSelectorWithMethodName:setIsKey value:value]) &#123;

        NSLog(@<span class="hljs-string">"*********%@**********"</span>,setIsKey);

        **<span class="hljs-keyword">return</span>**;

    &#125;

    

    <span class="hljs-comment">// 3: 判断是否响应 accessInstanceVariablesDirectly 返回YES NO 奔溃</span>

    <span class="hljs-comment">// 3:判断是否能够直接赋值实例变量</span>

    **<span class="hljs-keyword">if</span>** (![**self**.class accessInstanceVariablesDirectly] ) &#123;

        **@<span class="hljs-keyword">throw</span>** [NSException exceptionWithName:@<span class="hljs-string">"LGUnknownKeyException"</span> reason:[NSString stringWithFormat:@<span class="hljs-string">"****[%@ valueForUndefinedKey:]: this class is not key value coding-compliant for the key name.****"</span>,**self**] userInfo:**nil**];

    &#125;
    <span class="hljs-comment">// 4: 间接变量</span>

    <span class="hljs-comment">// 获取 ivar -> 遍历 containsObjct -</span>

    <span class="hljs-comment">// 4.1 定义一个收集实例变量的可变数组</span>

    NSMutableArray *mArray = [**self** getIvarListName];

    <span class="hljs-comment">// _<key> _is<Key> <key> is<Key></span>

    NSString *_key = [NSString stringWithFormat:@<span class="hljs-string">"_%@"</span>,key];

    NSString *_isKey = [NSString stringWithFormat:@<span class="hljs-string">"_is%@"</span>,Key];

    NSString *isKey = [NSString stringWithFormat:@<span class="hljs-string">"is%@"</span>,Key];

    **<span class="hljs-keyword">if</span>** ([mArray containsObject:_key]) &#123;

        <span class="hljs-comment">// 4.2 获取相应的 ivar</span>

       Ivar ivar = class_getInstanceVariable([**self** <span class="hljs-class"><span class="hljs-keyword">class</span>], <span class="hljs-title">_key</span>.<span class="hljs-title">UTF8String</span>)</span>;

        <span class="hljs-comment">// 4.3 对相应的 ivar 设置值</span>

       object_setIvar(**self** , ivar, value);

       **<span class="hljs-keyword">return</span>**;

    &#125;**<span class="hljs-keyword">else</span>** **<span class="hljs-keyword">if</span>** ([mArray containsObject:_isKey]) &#123;

       Ivar ivar = class_getInstanceVariable([**self** <span class="hljs-class"><span class="hljs-keyword">class</span>], <span class="hljs-title">_isKey</span>.<span class="hljs-title">UTF8String</span>)</span>;

       object_setIvar(**self** , ivar, value);

       **<span class="hljs-keyword">return</span>**;

    &#125;**<span class="hljs-keyword">else</span>** **<span class="hljs-keyword">if</span>** ([mArray containsObject:key]) &#123;

       Ivar ivar = class_getInstanceVariable([**self** <span class="hljs-class"><span class="hljs-keyword">class</span>], <span class="hljs-title">key</span>.<span class="hljs-title">UTF8String</span>)</span>;

       object_setIvar(**self** , ivar, value);

       **<span class="hljs-keyword">return</span>**;

    &#125;**<span class="hljs-keyword">else</span>** **<span class="hljs-keyword">if</span>** ([mArray containsObject:isKey]) &#123;

       Ivar ivar = class_getInstanceVariable([**self** <span class="hljs-class"><span class="hljs-keyword">class</span>], <span class="hljs-title">isKey</span>.<span class="hljs-title">UTF8String</span>)</span>;

       object_setIvar(**self** , ivar, value);

       **<span class="hljs-keyword">return</span>**;

    &#125;
    <span class="hljs-comment">// 5:如果找不到相关实例</span>

    **@<span class="hljs-keyword">throw</span>** [NSException exceptionWithName:@<span class="hljs-string">"LGUnknownKeyException"</span> reason:[NSString stringWithFormat:@<span class="hljs-string">"****[%@ %@]: this class is not key value coding-compliant for the key name.****"</span>,**self**,NSStringFromSelector( **_cmd**)] userInfo:**nil**];

    

&#125;
- (**nullable** **id**)lg_valueForKey:(NSString *)key&#123;

    

    <span class="hljs-comment">// 1:刷选key 判断非空</span>

    **<span class="hljs-keyword">if</span>** (key == **nil**  || key.length == <span class="hljs-number">0</span>) &#123;

        **<span class="hljs-keyword">return</span>** **nil**;

    &#125;

    <span class="hljs-comment">// 2:找到相关方法 get<Key> <key> countOf<Key>  objectIn<Key>AtIndex</span>

    <span class="hljs-comment">// key 要大写</span>

    NSString *Key = key.capitalizedString;

    <span class="hljs-comment">// 拼接方法</span>

    NSString *getKey = [NSString stringWithFormat:@<span class="hljs-string">"get%@"</span>,Key];

    NSString *countOfKey = [NSString stringWithFormat:@<span class="hljs-string">"countOf%@"</span>,Key];

    NSString *objectInKeyAtIndex = [NSString stringWithFormat:@<span class="hljs-string">"objectIn%@AtIndex:"</span>,Key];

        

#pragma clang diagnostic push

#pragma clang diagnostic ignored <span class="hljs-string">"-Warc-performSelector-leaks"</span>

    **<span class="hljs-keyword">if</span>** ([**self** respondsToSelector:NSSelectorFromString(getKey)]) &#123;

        **<span class="hljs-keyword">return</span>** [**self** performSelector:NSSelectorFromString(getKey)];

    &#125;**<span class="hljs-keyword">else</span>** **<span class="hljs-keyword">if</span>** ([**self** respondsToSelector:NSSelectorFromString(key)])&#123;

        **<span class="hljs-keyword">return</span>** [**self** performSelector:NSSelectorFromString(key)];

    &#125;**<span class="hljs-keyword">else</span>** **<span class="hljs-keyword">if</span>** ([**self** respondsToSelector:NSSelectorFromString(countOfKey)])&#123;

        **<span class="hljs-keyword">if</span>** ([**self** respondsToSelector:NSSelectorFromString(objectInKeyAtIndex)]) &#123;

            **int** num = (**int**)[**self** performSelector:NSSelectorFromString(countOfKey)];

            NSMutableArray *mArray = [NSMutableArray arrayWithCapacity:<span class="hljs-number">1</span>];

            **<span class="hljs-keyword">for</span>** (**int** i = <span class="hljs-number">0</span>; i<num-<span class="hljs-number">1</span>; i++) &#123;

                num = (**int**)[**self** performSelector:NSSelectorFromString(countOfKey)];

            &#125;

            **<span class="hljs-keyword">for</span>** (**int** j = <span class="hljs-number">0</span>; j<num; j++) &#123;

                **id** objc = [**self** performSelector:NSSelectorFromString(objectInKeyAtIndex) withObject:@(num)];

                [mArray addObject:objc];

            &#125;

            **<span class="hljs-keyword">return</span>** mArray;

        &#125;

    &#125;

#pragma clang diagnostic pop

    

    <span class="hljs-comment">// 3:判断是否能够直接赋值实例变量</span>

    **<span class="hljs-keyword">if</span>** (![**self**.class accessInstanceVariablesDirectly] ) &#123;

        **@<span class="hljs-keyword">throw</span>** [NSException exceptionWithName:@<span class="hljs-string">"LGUnknownKeyException"</span> reason:[NSString stringWithFormat:@<span class="hljs-string">"****[%@ valueForUndefinedKey:]: this class is not key value coding-compliant for the key name.****"</span>,**self**] userInfo:**nil**];

    &#125;

    

    <span class="hljs-comment">// 4.找相关实例变量进行赋值</span>

    <span class="hljs-comment">// 4.1 定义一个收集实例变量的可变数组</span>

    NSMutableArray *mArray = [**self** getIvarListName];

    <span class="hljs-comment">// _<key> _is<Key> <key> is<Key></span>

    <span class="hljs-comment">// _name -> _isName -> name -> isName</span>

    NSString *_key = [NSString stringWithFormat:@<span class="hljs-string">"_%@"</span>,key];

    NSString *_isKey = [NSString stringWithFormat:@<span class="hljs-string">"_is%@"</span>,Key];

    NSString *isKey = [NSString stringWithFormat:@<span class="hljs-string">"is%@"</span>,Key];

    **<span class="hljs-keyword">if</span>** ([mArray containsObject:_key]) &#123;

        Ivar ivar = class_getInstanceVariable([**self** <span class="hljs-class"><span class="hljs-keyword">class</span>], <span class="hljs-title">_key</span>.<span class="hljs-title">UTF8String</span>)</span>;

        **<span class="hljs-keyword">return</span>** object_getIvar(**self**, ivar);;

    &#125;**<span class="hljs-keyword">else</span>** **<span class="hljs-keyword">if</span>** ([mArray containsObject:_isKey]) &#123;

        Ivar ivar = class_getInstanceVariable([**self** <span class="hljs-class"><span class="hljs-keyword">class</span>], <span class="hljs-title">_isKey</span>.<span class="hljs-title">UTF8String</span>)</span>;

        **<span class="hljs-keyword">return</span>** object_getIvar(**self**, ivar);;

    &#125;**<span class="hljs-keyword">else</span>** **<span class="hljs-keyword">if</span>** ([mArray containsObject:key]) &#123;

        Ivar ivar = class_getInstanceVariable([**self** <span class="hljs-class"><span class="hljs-keyword">class</span>], <span class="hljs-title">key</span>.<span class="hljs-title">UTF8String</span>)</span>;

        **<span class="hljs-keyword">return</span>** object_getIvar(**self**, ivar);;

    &#125;**<span class="hljs-keyword">else</span>** **<span class="hljs-keyword">if</span>** ([mArray containsObject:isKey]) &#123;

        Ivar ivar = class_getInstanceVariable([**self** <span class="hljs-class"><span class="hljs-keyword">class</span>], <span class="hljs-title">isKey</span>.<span class="hljs-title">UTF8String</span>)</span>;

        **<span class="hljs-keyword">return</span>** object_getIvar(**self**, ivar);;

    &#125;
    **<span class="hljs-keyword">return</span>** @<span class="hljs-string">""</span>;

&#125;
#pragma mark **- 相关方法**

- (**BOOL**)lg_performSelectorWithMethodName:(NSString *)methodName value:(**id**)value&#123;

 

    **<span class="hljs-keyword">if</span>** ([**self** respondsToSelector:NSSelectorFromString(methodName)]) &#123;

        

#pragma clang diagnostic push

#pragma clang diagnostic ignored <span class="hljs-string">"-Warc-performSelector-leaks"</span>

        [**self** performSelector:NSSelectorFromString(methodName) withObject:value];

#pragma clang diagnostic pop

        **<span class="hljs-keyword">return</span>** **YES**;

    &#125;

    **<span class="hljs-keyword">return</span>** **NO**;

&#125;
- (**id**)performSelectorWithMethodName:(NSString *)methodName&#123;

    **<span class="hljs-keyword">if</span>** ([**self** respondsToSelector:NSSelectorFromString(methodName)]) &#123;

#pragma clang diagnostic push

#pragma clang diagnostic ignored <span class="hljs-string">"-Warc-performSelector-leaks"</span>

        **<span class="hljs-keyword">return</span>** [**self** performSelector:NSSelectorFromString(methodName) ];

#pragma clang diagnostic pop

    &#125;

    **<span class="hljs-keyword">return</span>** **nil**;

&#125;
- (NSMutableArray *)getIvarListName&#123;

    

    NSMutableArray *mArray = [NSMutableArray arrayWithCapacity:<span class="hljs-number">1</span>];

    **unsigned** **int** count = <span class="hljs-number">0</span>;

    Ivar *ivars = class_copyIvarList([**self** <span class="hljs-class"><span class="hljs-keyword">class</span>], &<span class="hljs-title">count</span>)</span>;

    **<span class="hljs-keyword">for</span>** (**int** i = <span class="hljs-number">0</span>; i<count; i++) &#123;

        Ivar ivar = ivars[i];

        **<span class="hljs-keyword">const</span>** **char** *ivarNameChar = ivar_getName(ivar);

        NSString *ivarName = [NSString stringWithUTF8String:ivarNameChar];

        NSLog(@<span class="hljs-string">"ivarName == %@"</span>,ivarName);

        [mArray addObject:ivarName];

    &#125;

    free(ivars);

    **<span class="hljs-keyword">return</span>** mArray;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">六.KVC拓展和总结</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90d7667c1c8e4844bec94164353406db~tplv-k3u1fbpfcp-watermark.image" alt="Xnip2021-08-08_16-11-31.jpg" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            