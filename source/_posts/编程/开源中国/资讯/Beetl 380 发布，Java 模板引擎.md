
---
title: 'Beetl 3.8.0 发布，Java 模板引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7690'
author: 开源中国
comments: false
date: Thu, 28 Oct 2021 02:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7690'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本次发布改善了 Function 功能，让 Beetl 在语法解析阶段能定制 Function</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>增加 LineAware 接口，实现此 Function 的函数，会在调用时候，在参数列表后追加一个所在行的参数，如 debug 函数,可以输出变量和调用时候所在的行</li> 
 <li>增加 ForceSafe 接口，实现此 Function 的函数，会在调用的时候，参数列表会增加一个安全输出符号，如 isEmpty 函数<span> </span><code>isEmpty(user)</code><span> </span>会变成<span> </span><code>isEmpty(user!)</code></li> 
 <li>增加 ChangeInput 接口，更加通用的方式，可以自定修改方法参数，如 has 函数<span> </span><code>has(var1)</code><span> </span>会更改为<span> </span><code>has("var1")</code></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">    Beetl 之前会有些”魔法函数“实现特殊功能，这次规范，只要实现如上接口，就可以实现各种魔法应用</p> 
<pre><code class="language-java">public interface Function &#123;

    /**
     * @param paras beetl传递的参数
     */
    Object call(Object[] paras, Context ctx);

/**
 * 如果Function实现了此接口，则会添加额当前外行参
 * @see org.beetl.ext.fn.DebugFunction
 */
static interface LineAware&#123;&#125;

/**
 * 如果Function还实现了此接口，则此函数参数将使用安全输出符号
 * @see org.beetl.ext.fn.IsNotEmptyExpressionFunction
 */
static  interface ForceSafe&#123;&#125;

/**
 * 如果Function实现了此接口，则入参会在解析的时候修改
 * @see org.beetl.ext.fn.CheckExistFunction
 *
 */
static interface  ChangeInput&#123;
public Expression[] update(GrammarCreator creator,Expression[] exps,GroupTemplate gt);
&#125;
&#125;
</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>对不符合 JavaBean 规范的 POJO，抛出异常的时候给与明确提示</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Beetl 是一款全功能，高性能优秀的国产模板引擎，各方面特性领先国外同类引擎技术,可以广泛用于动态页面生成，静态页面生成，代码生成，文本转换，脚本语言和规则引擎等，从 2011 年来一直维护，并得到国内公司用户的赞赏。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Maven</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-xml"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span></span>com.ibeetl<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span></span>beetl<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span></span>3.8.0.RELEASE<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span></span>
<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetl3_guide" target="_blank">文档</a> <a href="https://gitee.com/xiandafu/beetl">源码</a> <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fibeetl.com%2Fbeetlonline%2F" target="_blank">在线体验</a> <a href="https://gitee.com/xiandafu/template-benchmark">性能测试</a></p>
                                        </div>
                                      
</div>
            