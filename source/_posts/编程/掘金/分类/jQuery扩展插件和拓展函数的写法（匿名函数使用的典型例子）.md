
---
title: 'jQuery扩展插件和拓展函数的写法（匿名函数使用的典型例子）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=401'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 16:25:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=401'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这些年，javascript火起来了，主要归功于AJAX的推广应用，Web2.0的发展。。。于是，出现了很多的javascript框架。我选择了jQuery，最主要是它的思想“write less,do more"，因为我是一个挑剔的人，以前写过的代码，会时不时翻出来，看看有没有可以精简，优化的地方。一来是对不断学习的推动，二来可以将新的思想，技术应用到里面去。</p>
<p>对于jQuery插件的写法，以前就有介绍过，网上也有很多例子。 这里简要地进行些写法，主要是简写的说明，见下列代码：</p>
<pre><code class="copyable"><script type="text/javascript" src="jquery-1.4.2.js"></script>    

   <script type="text/javascript">

        //jQuery插件的写法（需要传入操作对象）
        ;(function($)
        &#123;
            //PI_TestPlugIn为插件名称，也是插件的操作对象
            //为了不会与其它插件名重复，这里我使用PlugIn的缩写PI_来定义插件对象前缀
            $.fn.PI_TestPlugIn=   
            &#123;
                //该插件的基本信息
                Info:&#123;
                    Name: "TestPlugIn",
                    Ver: "1.0.0.0",
                    Corp: "Lzhdim",
                    Author: "lzhdim",
                    Date: "2010-01-01 08:00:00",
                    Copyright: "Copyright @ 2000-2010 Lzhdim Technology Software All Rights Reserved",
                    License: "GPL"
                &#125;,
                //具有对象参数的函数，这里参数是一个对象，具有属性
                FunctionWithParams:function(paramObj)
                &#123;
                    //使用参数，是否使用默认值
                    var params = paramObj ? paramObj : &#123;
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　param1: "1",
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　param2: "2"
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　&#125;;

                   
                    return this.Info.Name + ".FunctionWithParamObject";
                &#125;,
                //具有参数的函数，这里参数是一个变量
                FunctionWithParam:function(varparam)
                &#123;
                    //使用参数，是否使用默认值
                    var param = varparam ? varparam : null;
                                                   
                    return this.Info.Name + ".FunctionWithParam";
                &#125;,
                //不具有参数的函数
                FunctionWithOutParam:function()
                &#123;
                    return  this.Info.Name + ".FunctionWithOutParam";
                &#125;
            &#125;;
        &#125;)(jQuery);
        
        
        //jQuery拓展函数的写法（不需要传入操作对象），即API函数
        ;(function($)
        &#123;
            $.extend(&#123;
                //FN_TestExtendFunction为拓展函数的操作对象
                //为了不会与其它插件名重复，这里我使用Extend的缩写FN_来定义函数对象前缀
                FN_TestExtendFunction:
                &#123;
                    //该拓展函数的基本信息
                    Info:&#123;
                        Name: "TestExtendFunction",
                        Ver: "1.0.0.0",
                        Corp: "Lzhdim",
                        Author: "lzhdim",
                        Date: "2010-01-01 08:00:00",
                        Copyright: "Copyright @ 2000-2010 Lzhdim Technology Software All Rights Reserved",
                        License: "GPL"
                    &#125;,
                    //具有对象参数的函数，这里参数是一个对象，具有属性
                    FunctionWithParams:function(paramObj)
                    &#123;
                        //使用参数，是否使用默认值
                        var params = paramObj ? paramObj : &#123;
                                                           param1: "1",
                                                           param2: "2"
                                                       &#125;;
                                                   
                                                   
                        return this.Info.Name + ".FunctionWithParamObect";
                    &#125;,
                    //具有参数的函数，这里参数是一个变量
                    FunctionWithParam: function (varparam) &#123;
                        //使用参数，是否使用默认值
                        var param = varparam ? varparam : null;

                        return this.FunctionWithOutParam() + ".FunctionWithParam";
                    &#125;,
                    //不具有参数的函数对象
                    FunctionWithOutParam:function()
                    &#123;
                        return this.Info.Name + ".FunctionWithOutParam";
                    &#125;
                &#125;
            &#125;);
        &#125;)(jQuery);



        $(function () 
        &#123;
            //测试插件
            var params = 
            &#123;
                param1: "3",
                param2: "4"
            &#125;;
 
　　　　　　　　alert(params.param1);
            
            alert($(this).PI_TestPlugIn.FunctionWithParams(params));

            alert($.FN_TestExtendFunction.FunctionWithParam(params));
        &#125;);
        
        
    </script>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            