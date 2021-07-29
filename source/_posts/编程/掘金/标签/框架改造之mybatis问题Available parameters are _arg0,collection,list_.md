
---
title: '框架改造之mybatis问题Available parameters are _arg0,collection,list_'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=4232'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 17:44:39 GMT
thumbnail: 'https://picsum.photos/400/300?random=4232'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>公司框架改造之后个别查询报错，错误如下</p>
<pre><code class="hljs language-sh copyable" lang="sh">Parameter <span class="hljs-string">"xxx"</span> not found.Available parameters are [arg0,collection,list]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调试代码如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">ParamNameResolver</span><span class="hljs-params">(Configuration config, Method method)</span> </span>&#123;
  <span class="hljs-keyword">this</span>.useActualParamName = config.isUseActualParamName();
  <span class="hljs-keyword">final</span> Class<?>[] paramTypes = method.getParameterTypes();
  <span class="hljs-keyword">final</span> Annotation[][] paramAnnotations = method.getParameterAnnotations();
  <span class="hljs-keyword">final</span> SortedMap<Integer, String> map = <span class="hljs-keyword">new</span> TreeMap<>();
  <span class="hljs-keyword">int</span> paramCount = paramAnnotations.length;
  <span class="hljs-comment">// get names from @Param annotations</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> paramIndex = <span class="hljs-number">0</span>; paramIndex < paramCount; paramIndex++) &#123;
    <span class="hljs-keyword">if</span> (isSpecialParameter(paramTypes[paramIndex])) &#123;
      <span class="hljs-comment">// skip special parameters</span>
      <span class="hljs-keyword">continue</span>;
    &#125;
    String name = <span class="hljs-keyword">null</span>;
    <span class="hljs-keyword">for</span> (Annotation annotation : paramAnnotations[paramIndex]) &#123;
      <span class="hljs-keyword">if</span> (annotation <span class="hljs-keyword">instanceof</span> Param) &#123;
        hasParamAnnotation = <span class="hljs-keyword">true</span>;
        name = ((Param) annotation).value();
        <span class="hljs-keyword">break</span>;
      &#125;
    &#125;
    <span class="hljs-keyword">if</span> (name == <span class="hljs-keyword">null</span>) &#123;
      <span class="hljs-comment">// @Param was not specified.</span>
      <span class="hljs-keyword">if</span> (useActualParamName) &#123;
        name = getActualParamName(method, paramIndex);
      &#125;
      <span class="hljs-keyword">if</span> (name == <span class="hljs-keyword">null</span>) &#123;
        <span class="hljs-comment">// use the parameter index as the name ("0", "1", ...)</span>
        <span class="hljs-comment">// gcode issue #71</span>
        name = String.valueOf(map.size());
      &#125;
    &#125;
    map.put(paramIndex, name);
  &#125;
  names = Collections.unmodifiableSortedMap(map);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于代码中只有单参数，沒有使用<code>@Param</code>注解，并且使用的编译插件不是<code>springboot-starter-parent</code>中的插件。其实这边主要时<code>parameter</code>s这个参数设置为<code>true</code>即可</p>
<pre><code class="copyable"><plugin>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <parameters>true</parameters>
    </configuration>
</plugin>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此参数为<code>javac</code>的参数<code>javac -parameters</code>
不加此参数编译出来的的参数为<code>arg0,arg1</code>,加了此参数则就会使用参数名。
而<code>mybatis</code>中</p>
<pre><code class="copyable">if (useActualParamName) &#123;
  name = getActualParamName(method, paramIndex);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>useActualParamName</code>此属性为<code>true</code>时就会通过<code>jvm</code>获取到实际参数名称。所以就产生了如上报错。
当加上了这个参数之后就正常了，但是问题还没结束，这个外包项目有个自己写的<code>db</code>框架。第二天其它的项目又出了个问题
<code>Parameter "arg0" not found.Available parameters are [param1,xxx,yyy,param2]</code>调试发现代码如下</p>
<pre><code class="copyable">public class BaseSQLBuilder &#123;

    public final static String SCRIPT_PREFIX = "<script>";
    public final static String SCRIPT_SUFFIX = "</script>";
    public final static String ARG_0 = "arg0";

    public String buildBySQL(Map<String, Object> params) &#123;
        Assert.notEmpty(params, "Parameter params cannot be null or empty");

        return joinScriptXml(params.get(ARG_0) + StringUtils.EMPTY);
    &#125;

    private String joinScriptXml(String value) &#123;
        StringBuilder builder = new StringBuilder();
        builder.append(SCRIPT_PREFIX).append(value).append(SCRIPT_SUFFIX);

        return builder.toString();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个<code>db</code>框架构建<code>sql</code>时偷了个懒写死了取<code>arg0</code>怎么办呢？
没关系呢，这个只是编译阶段的产物，所以单独把这个db框架不加parameter参数编译即可。</p></div>  
</div>
            