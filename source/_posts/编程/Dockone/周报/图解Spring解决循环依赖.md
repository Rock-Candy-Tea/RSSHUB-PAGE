
---
title: '图解Spring解决循环依赖'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210903/76fc0e08833cc9cdc9f4c22073d6e760.png'
author: Dockone
comments: false
date: 2021-09-06 15:07:46
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210903/76fc0e08833cc9cdc9f4c22073d6e760.png'
---

<div>   
<br><h3>前言</h3><strong>Spring</strong>如何解决的循环依赖，是近两年流行起来的一道Java面试题。<br>
<br>其实笔者本人对这类<strong>框架源码题</strong>还是持一定的怀疑态度的。<br>
<br>如果笔者作为面试官，可能会问一些诸如“如果注入的属性为<strong>null</strong>，你会从哪几个方向去排查”这些<strong>场景题</strong>。<br>
<br>那么既然写了这篇文章，闲话少说，发车看看<strong>Spring是如何解决的循环依赖</strong>，以及带大家看清循环依赖的本质是什么。<br>
<h3>正文</h3>通常来说，如果问Spring内部如何解决循环依赖，一定是单默认的<strong>单例</strong>Bean中，属性互相引用的场景。<br>
<br>比如几个Bean之间的互相引用：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210903/76fc0e08833cc9cdc9f4c22073d6e760.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210903/76fc0e08833cc9cdc9f4c22073d6e760.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
甚至自己“循环”依赖自己：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210903/7fbb78f25a2c1ec7200dee43e65b42e7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210903/7fbb78f25a2c1ec7200dee43e65b42e7.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
先说明前提：<strong>原型</strong>（Prototype）的场景是<strong>不支持</strong>循环依赖的，通常会走到<code class="prettyprint">AbstractBeanFactory</code>类中下面的判断，抛出异常。<br>
<pre class="prettyprint">if (isPrototypeCurrentlyInCreation(beanName)) &#123;  <br>
throw new BeanCurrentlyInCreationException(beanName);  <br>
&#125; <br>
</pre><br>
原因很好理解，创建<strong>新的A</strong>时，发现要注入<strong>原型字段B</strong>，又创建<strong>新的B</strong>发现要注入<strong>原型字段A</strong>……<br>
<br>这就套娃了, 你猜是先<strong>StackOverflow</strong>还是<strong>OutOfMemory</strong>？<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210903/6420d2d0cf35986e96b6832a6faff303.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210903/6420d2d0cf35986e96b6832a6faff303.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
基于构造器的循环依赖，就更不用说了，<a href="https://docs.spring.io/spring/docs/current/spring-framework-reference/core.html#beans-dependency-resolution">官方文档</a>都摊牌了，你想让构造器注入支持循环依赖，是不存在的，不如把代码改了。<br>
<br>那么默认单例的属性注入场景，<strong>Spring</strong>是如何支持循环依赖的？<br>
<h4>Spring解决循环依赖</h4>首先，Spring内部维护了三个<strong>Map</strong>，也就是我们通常说的<strong>三级缓存</strong>。<br>
<br>笔者翻阅Spring文档倒是没有找到三级缓存的概念，可能也是本土为了方便理解的词汇。<br>
<br>在Spring的<code class="prettyprint">DefaultSingletonBeanRegistry</code>类中，你会赫然发现类上方挂着这三个Map：<br>
<ul><li>singletonObjects，它是我们最熟悉的朋友，俗称“<strong>单例池</strong>”“<strong>容器</strong>”，缓存创建完成单例Bean的地方。</li><li>singletonFactories，映射创建Bean的原始工厂</li><li>earlySingletonObjects，映射Bean的<strong>早期</strong>引用，也就是说在这个Map里的Bean不是完整的，甚至还不能称之为“<strong>Bean</strong>”，只是一个<strong>Instance</strong>。</li></ul><br>
<br>后两个Map其实是“<strong>垫脚石</strong>”级别的，只是创建Bean的时候，用来借助了一下，创建完成就清掉了。<br>
<br>所以笔者前文对“三级缓存”这个词有些迷惑，可能是因为注释都是以Cache of开头吧。<br>
<br>为什么成为后两个Map为<strong>垫脚石</strong>，假设最终放在<strong>singletonObjects</strong>的Bean是你想要的一杯“凉白开”。<br>
<br>那么Spring准备了两个杯子，即singletonFactories和earlySingletonObjects来回“倒腾”几番，把热水晾成“凉白开”放到<strong>singletonObjects</strong>中。<br>
<br>闲话不说，都浓缩在图里。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210903/3e6bdd37e5f9ac55fa3636708f79034e.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210903/3e6bdd37e5f9ac55fa3636708f79034e.gif" class="img-polaroid" title="4.gif" alt="4.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
上面的是一张GIF，如果你没看到可能还没加载出来。（三秒一帧，不是你电脑卡。）<br>
<br>笔者画了17张图<strong>简化表述</strong>了Spring的主要步骤，GIF上方即是刚才提到的三级缓存，下方展示是<strong>主要</strong>的几个方法。<br>
<br>当然了，这个地步你肯定要结合<a href="https://github.com/spring-projects/spring-framework">Spring源码</a>来看，要不肯定看不懂。<br>
<br>如果你只是想大概了解，或者面试，可以先记住笔者上文提到的“<strong>三级缓存</strong>”，以及下文即将要说的本质。<br>
<h4>循环依赖的本质</h4>上文了解完Spring如何处理循环依赖之后，让我们跳出“<strong>阅读源码</strong>”的思维，假设让你实现一个有以下特点的功能，你会怎么做？<br>
<ul><li>将指定的一些类实例为单例</li><li>类中的字段也都实例为单例</li><li>支持循环依赖</li></ul><br>
<br>举个例子，假设有类A：<br>
<pre class="prettyprint">public class A &#123;  <br>
private B b;  <br>
&#125; <br>
</pre><br>
类B：<br>
<pre class="prettyprint">public class B &#123;  <br>
private A a;  <br>
&#125; <br>
</pre><br>
说白了让你<strong>模仿Spring</strong>：<strong>假装A</strong>和<strong>B</strong>是被@Component修饰，<br><br>
并且类中的字段<strong>假装</strong>是@Autowired修饰的，处理完放到Map中。<br>
<br>其实非常简单，笔者写了一份粗糙的代码，可供参考：<br>
<pre class="prettyprint">/**  <br>
 * 放置创建好的bean Map  <br>
 */  <br>
private static Map<String, Object> cacheMap = new HashMap<>(2);  <br>
<br>
public static void main(String[] args) &#123;  <br>
    // 假装扫描出来的对象  <br>
    Class[] classes = &#123;A.class, B.class&#125;;  <br>
    // 假装项目初始化实例化所有bean  <br>
    for (Class aClass : classes) &#123;  <br>
        getBean(aClass);  <br>
    &#125;  <br>
    // check  <br>
    System.out.println(getBean(B.class).getA() == getBean(A.class));  <br>
    System.out.println(getBean(A.class).getB() == getBean(B.class));  <br>
&#125;  <br>
<br>
@SneakyThrows  <br>
private static <T> T getBean(Class<T> beanClass) &#123;  <br>
    // 本文用类名小写 简单代替bean的命名规则  <br>
    String beanName = beanClass.getSimpleName().toLowerCase();  <br>
    // 如果已经是一个bean，则直接返回  <br>
    if (cacheMap.containsKey(beanName)) &#123;  <br>
        return (T) cacheMap.get(beanName);  <br>
    &#125;  <br>
    // 将对象本身实例化  <br>
    Object object = beanClass.getDeclaredConstructor().newInstance();  <br>
    // 放入缓存  <br>
    cacheMap.put(beanName, object);  <br>
    // 把所有字段当成需要注入的bean，创建并注入到当前bean中  <br>
    Field[] fields = object.getClass().getDeclaredFields();  <br>
    for (Field field : fields) &#123;  <br>
        field.setAccessible(true);  <br>
        // 获取需要注入字段的class  <br>
        Class<?> fieldClass = field.getType();  <br>
        String fieldBeanName = fieldClass.getSimpleName().toLowerCase();  <br>
        // 如果需要注入的bean，已经在缓存Map中，那么把缓存Map中的值注入到该field即可  <br>
        // 如果缓存没有 继续创建  <br>
        field.set(object, cacheMap.containsKey(fieldBeanName)  <br>
                ? cacheMap.get(fieldBeanName) : getBean(fieldClass));  <br>
    &#125;  <br>
    // 属性填充完成，返回  <br>
    return (T) object;  <br>
&#125; <br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210903/f3dfdd69aed891865b37f04687b2a68e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210903/f3dfdd69aed891865b37f04687b2a68e.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这就是“<strong>循环依赖</strong>”的本质，而不是“Spring如何解决循环依赖”。<br>
<br>之所以要举这个例子，是发现一小部分盆友陷入了“<strong>阅读源码的泥潭</strong>”，而忘记了问题的本质。<br>
<br>为了看源码而看源码，结果一直看不懂，却忘了本质是什么。<br>
<br>如果真看不懂，不如先写出基础版本，逆推Spring为什么要这么实现，可能效果会更好。<br>
<br><strong>What？问题的本质居然是two sum！</strong><br>
<br>看完笔者刚才的代码有没有似曾相识？没错，和<strong>two sum</strong>的解题是类似的。<br>
<br>不知道<strong>two sum</strong>是什么梗的，笔者和你介绍一下：<br>
<br><strong>two sum</strong>是刷题网站<a href="https://leetcode-cn.com/problems/two-sum/">LeetCode</a>序号为1的题，也就是大多人的算法入门的第一题。<br>
<br>常常被人调侃，有<strong>算法面</strong>的公司，被面试官钦定了，合的来。那就来一道<strong>two sum</strong>走走过场。<br>
<br>问题内容是：给定<strong>一个数组</strong>，给定<strong>一个数字</strong>。返回数组中可以<strong>相加得到指定数字</strong>的两个<strong>索引</strong>。<br>
<br>比如：给定<code class="prettyprint">nums = [2, 7, 11, 15], target = 9</code>，那么要返回<code class="prettyprint">[0, 1]</code>，因为<code class="prettyprint">2 + 7 = 9</code>。<br>
<br>这道题的优解是，一次遍历+HashMap：<br>
<pre class="prettyprint">class Solution &#123;  <br>
public int[] twoSum(int[] nums, int target) &#123;  <br>
    Map<Integer, Integer> map = new HashMap<>();  <br>
    for (int i = 0; i < nums.length; i++) &#123;  <br>
        int complement = target - nums[i];  <br>
        if (map.containsKey(complement)) &#123;  <br>
            return new int[] &#123; map.get(complement), i &#125;;  <br>
        &#125;  <br>
        map.put(nums[i], i);  <br>
    &#125;  <br>
    throw new IllegalArgumentException("No two sum solution");  <br>
&#125;  <br>
&#125;  <br>
//作者：LeetCode  <br>
//链接：https://leetcode-cn.com/problems/two-sum/solution/liang-shu-zhi-he-by-leetcode-2/  <br>
//来源：力扣（LeetCode）<br>
</pre><br>
先去Map中找<strong>需要的数字</strong>，没有就将<strong>当前的数字</strong>保存在Map中，如果找到<strong>需要的数字</strong>，则一起返回。<br>
<br>和笔者上面的代码是不是一样？<br>
<br>先去缓存里找<strong>Bean</strong>，没有则<strong>实例化当前的Bean</strong>放到Map，如果有需要<strong>依赖</strong>当前Bean的，就能从Map取到。<br>
<h3>结尾</h3>如果你是上文笔者提到的“<strong>陷入阅读源码的泥潭</strong>”的读者，上文应该可以帮助到你。<br>
<br>可能还有盆友有疑问，为什么一道“<strong>two-sum</strong>”，Spring处理的如此复杂？  <br>
<br>这个想想Spring支持多少功能就知道了，各种实例方式..各种注入方式..各种Bean的加载，校验..各种<strong>callback</strong>，aop处理等等..<br>
<br>Spring可不只有<strong>依赖注入</strong>，同样Java也不仅是<strong>Spring</strong>。如果我们陷入了某个“牛角尖”，不妨跳出来看看，可能会更佳清晰哦。<br>
<br>原文链接：<a href="https://juejin.cn/post/6844904122160775176" rel="nofollow" target="_blank">https://juejin.cn/post/6844904122160775176</a>，作者：Vt
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            