
---
title: '一套iOS底层试卷-我想和你分享'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=1810'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 22:06:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=1810'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">考试介绍</h3>
<p>最近一直在带大师班,学习有一段时间了带着以下三个目的进行了一场测验.收益颇多.这里也纪录下来</p>
<p>🎯 考试检测大家最近的学习</p>
<p>🎯 敲响警钟,希望大家能够端正学习态度、及时查漏补缺</p>
<p>🎯 根据大家在这阶段学习的情况调整下阶段讲课的速度和深度</p>
<p>正常考试 分为四种题型. 总分 200分 (不要问我为什么不是100分,诶...就是玩!!!!😸)</p>
<ul>
<li>
<p>1、选择题 (每题5分, 共10道 50分)</p>
</li>
<li>
<p>2、判断题 (每题5分, 共6道 30分)</p>
</li>
<li>
<p>3、简单题 (每题10分 共10道 100分)</p>
</li>
<li>
<p>4、拓展满分题 (20分)</p>
</li>
</ul>
<blockquote>
<p>下面我就贴出题目吧,如果你有时间的,不妨也拿笔本子测试一下,看看能做多少分,在文章留言我会第一时间发你答案! 或者加我微信: KC_Cooci</p>
</blockquote>
<h3 data-id="heading-1">一、选择题(每题5分) ⚠️ 有单选有多选哦⚠️</h3>
<blockquote>
<ul>
<li>
<ol>
<li>在LP64下,一个指针的有多少个字节  分值5分</li>
</ol>
</li>
</ul>
</blockquote>
<ul class="contains-task-list">
<li class="task-list-item">
<p><input type="checkbox" disabled>  A: 4</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> B: 8</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> C: 16</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled>  D: 64</p>
</li>
</ul>
<blockquote>
<ul>
<li>
<ol start="2">
<li>一个实例对象的内存结构存在哪些元素  分值5分</li>
</ol>
</li>
</ul>
</blockquote>
<ul class="contains-task-list">
<li class="task-list-item">
<p><input type="checkbox" disabled> A:成员变量</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> B: supClass</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> C: cache_t</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> D: bit</p>
</li>
</ul>
<blockquote>
<ul>
<li>
<ol start="3">
<li>下面<code>sizeof(struct3)</code> 大小等于  分值5分</li>
</ol>
</li>
</ul>
</blockquote>
<pre><code class="copyable">struct LGStruct1 &#123;
    char b;
    int c;
    double a;
    short d;
&#125;struct1;

struct LGStruct2 &#123;
    double a;
    int b;
    char c;
    short d;
&#125;struct2;


struct LGStruct3 &#123;
    double a;
    int b;
    char c;
    struct LGStruct1 str1;
    short d;
    int e;
    struct LGStruct2 str2;
&#125;struct3;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul class="contains-task-list">
<li class="task-list-item">
<p><input type="checkbox" disabled> A: 48</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> B: 56</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> C: 64</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> D: 72</p>
</li>
</ul>
<blockquote>
<ul>
<li>
<ol start="4">
<li>下列代码: <code>re1 re2 re3 re4 re5 re6 re7</code> re8输出结果  分值5分</li>
</ol>
</li>
</ul>
</blockquote>
<pre><code class="copyable">BOOL re1 = [(id)[NSObject class] isKindOfClass:[NSObject class]];     
BOOL re2 = [(id)[NSObject class] isMemberOfClass:[NSObject class]];   
BOOL re3 = [(id)[LGPerson class] isKindOfClass:[LGPerson class]];     
BOOL re4 = [(id)[LGPerson class] isMemberOfClass:[LGPerson class]];  
NSLog(@" re1 :%hhd\n re2 :%hhd\n re3 :%hhd\n re4 :%hhd\n",re1,re2,re3,re4);

BOOL re5 = [(id)[NSObject alloc] isKindOfClass:[NSObject class]];      
BOOL re6 = [(id)[NSObject alloc] isMemberOfClass:[NSObject class]];    
BOOL re7 = [(id)[LGPerson alloc] isKindOfClass:[LGPerson class]];     
BOOL re8 = [(id)[LGPerson alloc] isMemberOfClass:[LGPerson class]];   
NSLog(@" re5 :%hhd\n re6 :%hhd\n re7 :%hhd\n re8 :%hhd\n",re5,re6,re7,re8);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul class="contains-task-list">
<li class="task-list-item">
<p><input type="checkbox" disabled> A: 1011 1111</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> B: 1100 1011</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> C: 1000 1111</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> D: 1101 1111</p>
</li>
</ul>
<blockquote>
<ul>
<li>
<ol start="5">
<li><code>(x + 7) & ~7</code> 这个算法是几字节对齐  分值5分</li>
</ol>
</li>
</ul>
</blockquote>
<ul class="contains-task-list">
<li class="task-list-item">
<p><input type="checkbox" disabled> A: 7</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> B: 8</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> C: 14</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> D: 16</p>
</li>
</ul>
<blockquote>
<ul>
<li>
<ol start="6">
<li>判断下列数据结构大小  分值5分</li>
</ol>
</li>
</ul>
</blockquote>
<pre><code class="copyable">union kc_t &#123;
    uintptr_t bits;
    struct &#123;
        int a;
        char b;
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul class="contains-task-list">
<li class="task-list-item">
<p><input type="checkbox" disabled> A: 8</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> B: 12</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> C: 13</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> D: 16</p>
</li>
</ul>
<blockquote>
<ul>
<li>
<ol start="7">
<li>元类的 isa 指向谁, 根元类的父类是谁  分值5分</li>
</ol>
</li>
</ul>
</blockquote>
<ul class="contains-task-list">
<li class="task-list-item">
<p><input type="checkbox" disabled> A: 自己 , 根元类</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> B: 自己 , NSObject</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> C: 根元类 , 根元类</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> D: 根元类 , NSObject</p>
</li>
</ul>
<blockquote>
<ul>
<li>
<ol start="8">
<li>查找方法缓存的时候发现是乱序的, 为什么? 哈希冲突怎么解决的  分值5分</li>
</ol>
</li>
</ul>
</blockquote>
<ul class="contains-task-list">
<li class="task-list-item">
<p><input type="checkbox" disabled> A: 哈希函数原因 , 不解决</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> B: 哈希函数原因 , 再哈希</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> C: 他存他的我也布吉岛 , 再哈希</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> D: 他乱由他乱,清风过山岗 , 不解决</p>
</li>
</ul>
<blockquote>
<ul>
<li>
<ol start="9">
<li>消息的流程是  分值5分</li>
</ol>
</li>
</ul>
</blockquote>
<ul class="contains-task-list">
<li class="task-list-item">
<p><input type="checkbox" disabled> A: 先从缓存快速查找</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> B: 慢速递归查找methodlist (自己的和父类的,直到父类为nil)</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> C: 动态方法决议</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> D: 消息转发流程</p>
</li>
</ul>
<blockquote>
<ul>
<li>
<ol start="10">
<li>类方法动态方法决议为什么在后面还要实现 <code>resolveInstanceMethod</code>   分值5分</li>
</ol>
</li>
</ul>
</blockquote>
<ul class="contains-task-list">
<li class="task-list-item">
<p><input type="checkbox" disabled> A: 类方法存在元类(以对象方法形式存在), 元类的父类最终是 <code>NSObject</code> 所以我们可以通过<code>resolveInstanceMethod</code> 防止 <code>NSObject</code> 中实现了对象方法!</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> B: 因为在oc的底层最终还是对象方法存在</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> C: 类方法存在元类以对象方法形式存在.</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> D: 咸吃萝卜,淡操心! 苹果瞎写的 不用管</p>
</li>
</ul>
<h3 data-id="heading-2">二、判断题 (每题5分)</h3>
<blockquote>
<ul>
<li>
<ol start="11">
<li>光凭我们的对象地址,无法确认对象是否存在关联对象  分值5分</li>
</ol>
</li>
</ul>
</blockquote>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 对</li>
<li class="task-list-item"><input type="checkbox" disabled> 错</li>
</ul>
<blockquote>
<ul>
<li>
<ol start="12">
<li><code>int c[4] = &#123;1,2,3,4&#125;; int *d = c; c[2] = *(d+2)</code>  分值5分</li>
</ol>
</li>
</ul>
</blockquote>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 对</li>
<li class="task-list-item"><input type="checkbox" disabled> 错</li>
</ul>
<blockquote>
<ul>
<li>
<ol start="13">
<li><code>@interface LGPerson : NSObject&#123; UIButton *btn &#125;</code> 其中 <code>btn</code> 是实例变量  分值5分</li>
</ol>
</li>
</ul>
</blockquote>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 对</li>
<li class="task-list-item"><input type="checkbox" disabled> 错</li>
</ul>
<blockquote>
<ul>
<li>
<ol start="14">
<li><code>NSObject</code> 除外 元类的父类 = 父类的元类  分值5分</li>
</ol>
</li>
</ul>
</blockquote>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 对</li>
<li class="task-list-item"><input type="checkbox" disabled> 错</li>
</ul>
<blockquote>
<ul>
<li>
<ol start="15">
<li>对象的地址就是内存元素的首地址  分值5分</li>
</ol>
</li>
</ul>
</blockquote>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 对</li>
<li class="task-list-item"><input type="checkbox" disabled> 错</li>
</ul>
<blockquote>
<ul>
<li>
<ol start="16">
<li>类也是对象  分值5分</li>
</ol>
</li>
</ul>
</blockquote>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 对</li>
<li class="task-list-item"><input type="checkbox" disabled> 错</li>
</ul>
<h3 data-id="heading-3">三、简单题 (每题 10分 合计 100分)</h3>
<p><strong>请把它当成一场面试,认真对待 希望大家耐心 切忌浮躁 (和谐学习 不急不躁)</strong></p>
<ul>
<li>
<p>17、怎么将上层OC代码还原成 <code>C++</code>代码  分值10分</p>
</li>
<li>
<p>18、怎么打开汇编查看流程,有什么好处 ?  分值10分</p>
</li>
<li>
<p>19、<code>x/4gx</code> 和 <code>p/x</code> 以及 <code>p *$0</code> 代表什么意思  分值10分</p>
</li>
<li>
<p>20、类方法存在哪里? 为什么要这么设计?  分值10分</p>
</li>
<li>
<p>21、方法慢速查找过程中的二分查找流程,请用伪代码实现 分值10分</p>
</li>
<li>
<p>22、<code>ISA_MASK = 0x00007ffffffffff8ULL</code> 那么这个 <code>ISA_MASK</code> 的算法意义是什么?  分值10分</p>
</li>
<li>
<p>23、类的结构里面为什么会有 <code>rw</code> 和 <code>ro</code> 以及 <code>rwe</code> ?  分值10分</p>
</li>
<li>
<p>24、<code>cache</code> 在什么时候开始扩容 , 为什么?  分值10分</p>
</li>
<li>
<p>25、<code>objc_msgSend</code> 为什么用汇编写 , <code>objc_msgSend</code> 是如何递归找到imp?  分值10分</p>
</li>
<li>
<p>26、一个类的类方法没有实现为什么可以调用 <code>NSObject</code> 同名对象方法  分值10分</p>
</li>
</ul>
<h3 data-id="heading-4">四、拓展满分题 (20分</h3>
<ol start="27">
<li>提交一篇大师班学习期间,你写的最好的一篇博客  分值20分</li>
</ol>
<h3 data-id="heading-5">五、总结</h3>
<p>考试的题目偏向底层, 也比较贴合现在iOS的面试市场! 内容有深有浅,还可以继续挖坑 (👀)</p>
<blockquote>
<p>声明: 内容只是为了促进学习,并不是为行业增加内卷.希望各位靓仔靓女 不要把这些题目作为面试素材为难求职者.答案可以直接微信我: KC_Cooci</p>
</blockquote></div>  
</div>
            