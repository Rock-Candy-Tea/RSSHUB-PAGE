
---
title: 'LiteFlow 2.6.4 版本发行注记，里程碑版本!'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1176'
author: 开源中国
comments: false
date: Fri, 12 Nov 2021 11:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1176'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:30px; margin-right:30px"><span>一</span><span> </span></h2> 
<p style="color:black; margin-left:0; margin-right:0">这个版本做的很折腾。期间几个issue推翻重做了好几次。</p> 
<p style="color:black; margin-left:0; margin-right:0">但我最终还是带来了LiteFlow 2.6.4这个重要版本。</p> 
<p style="color:black; margin-left:0; margin-right:0">虽然版本是小版本号升级，但是带来的更新可一点也不少。并完全向下兼容。</p> 
<p style="color:black; margin-left:0; margin-right:0">如果你是第一次知道LiteFlow这款框架，可以移步以下链接进行了解：</p> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">官网：https://yomahub.com/liteflow</p> 
 <p style="color:black; margin-left:0; margin-right:0">Gitee仓库主页：https://gitee.com/dromara/liteFlow</p> 
 <p style="color:black; margin-left:0; margin-right:0">Github仓库主页：https://github.com/dromara/liteflow</p> 
</blockquote> 
<p style="color:black; margin-left:0; margin-right:0">也可以看我之前发布的一篇介绍LiteFlow框架的文章</p> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">https://mp.weixin.qq.com/s/xyydmtk_a5R1zbg3EeORaw</p> 
</blockquote> 
<h2 style="margin-left:30px; margin-right:30px"><span>二</span><span> </span></h2> 
<p style="color:black; margin-left:0; margin-right:0">这次的新版本带来了4个特性，4个增强，4个修复。总共12个issue的更新。</p> 
<p style="color:black; margin-left:0; margin-right:0">重点说下几个重要的更新点</p> 
<p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">支持文件脚本的定义</strong></p> 
<p style="color:black; margin-left:0; margin-right:0">你除了可以把脚本内容写在配置文件中，也可以写在文件中。如果大的脚本就推荐写在文件中。毕竟IDE对文件的语法高亮和代码提示做的也相对友好。编写脚本会更加方便。</p> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">文档位置：https://yomahub.com/liteflow/docs/user-detail-guide/user-detail-guide-script</p> 
</blockquote> 
<p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">支持链路的前置和后置节点</strong></p> 
<p style="color:black; margin-left:0; margin-right:0">新版本支持了前置组件和后置组件特性。</p> 
<p style="color:black; margin-left:0; margin-right:0">此特性针对整个链路，在链路之前之后固定执行某些组件。用于业务的前置处理和后置处理。</p> 
<p style="color:black; margin-left:0; margin-right:0">其中后置节点不受Exception影响，即便节点出错，后置节点依旧会执行。</p> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">文档位置：https://yomahub.com/liteflow/docs/user-detail-guide/user-detail-guide-pre-and-finally</p> 
</blockquote> 
<p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">优雅平滑刷新的支持</strong></p> 
<p style="color:black; margin-left:0; margin-right:0">这个功能被催了好久，之前的版本因为不平滑刷新，热更新方面总感觉差点意思。</p> 
<p style="color:black; margin-left:0; margin-right:0">这次新版本带来了完全平滑的热刷新机制，分为主动刷新和被动刷新2个接口。在高并发时也不会担心因为刷新规则而导致的链路执行异常了。</p> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">文档位置：https://yomahub.com/liteflow/docs/user-detail-guide/user-detail-guide-refresh</p> 
</blockquote> 
<p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">并行节点中任意节点结束即继续的流程支持</strong></p> 
<p style="color:black; margin-left:0; margin-right:0">对并行节点做了进一步的流程特性支持。根据这个特性，你可以编排出更加灵活的流程设计。</p> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">文档位置：https://yomahub.com/liteflow/docs/user-detail-guide/user-detail-guide-condition</p> 
</blockquote> 
<h2 style="margin-left:30px; margin-right:30px"><span>三</span><span> </span></h2> 
<p style="color:black; margin-left:0; margin-right:0">本次2.6.4除了一些特性和增强。最大的改动就是重写了底层的异步线程模型。</p> 
<p style="color:black; margin-left:0; margin-right:0">本来想集成asyncTool作为线程编排的核心，但是做了一版之后发现有些细节没办法很好的兼容。于是根据asyncTool的核心思想，重写了异步线程模型以适配liteflow的异步线程编排。</p> 
<p style="color:black; margin-left:0; margin-right:0">在这里，感谢asyncTool这个项目和其项目作者京东武伟峰，在开发这个版本时候给了解答了我一些技术疑惑。</p> 
<h2 style="margin-left:30px; margin-right:30px"><span>四</span><span> </span></h2> 
<p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">完整更新列表如下：</strong></p> 
<p style="color:black; margin-left:0; margin-right:0">特性 #I4GYV2 script节点支持从文件中获取脚本</p> 
<p style="color:black; margin-left:0; margin-right:0">https://gitee.com/dromara/liteFlow/issues/I4GYV2</p> 
<p style="color:black; margin-left:0; margin-right:0">特性 #I4HGOW 支持链路的前置和后置节点</p> 
<p style="color:black; margin-left:0; margin-right:0">https://gitee.com/dromara/liteFlow/issues/I4HGOW</p> 
<p style="color:black; margin-left:0; margin-right:0">特性 #I4FSHW 优雅平滑刷新的支持</p> 
<p style="color:black; margin-left:0; margin-right:0">https://gitee.com/dromara/liteFlow/issues/I4FSHW</p> 
<p style="color:black; margin-left:0; margin-right:0">特性 #I4GS03 并行节点中支持任意节点结束即继续的流程设计</p> 
<p style="color:black; margin-left:0; margin-right:0">https://gitee.com/dromara/liteFlow/issues/I4GS03</p> 
<p style="color:black; margin-left:0; margin-right:0">增强 #I4HKZG 借鉴asyncTool对异步线程底层进行了彻底重构</p> 
<p style="color:black; margin-left:0; margin-right:0">https://gitee.com/dromara/liteFlow/issues/I4HKZG</p> 
<p style="color:black; margin-left:0; margin-right:0">增强 #I4HD8L 支持异步节点返回自定义的错误</p> 
<p style="color:black; margin-left:0; margin-right:0">https://gitee.com/dromara/liteFlow/issues/I4HD8L</p> 
<p style="color:black; margin-left:0; margin-right:0">增强 #I4GZ1Q 增强异步线程超时的情况下打印出具体超时节点的信息</p> 
<p style="color:black; margin-left:0; margin-right:0">https://gitee.com/dromara/liteFlow/issues/I4GZ1Q</p> 
<p style="color:black; margin-left:0; margin-right:0">增强 #I4EXCP 新增 自定义 关闭/启动 Banner</p> 
<p style="color:black; margin-left:0; margin-right:0">https://gitee.com/dromara/liteFlow/issues/I4EXCP</p> 
<p style="color:black; margin-left:0; margin-right:0">修复 #I4GY9L 在启动后马上刷新流程后会有offerSlot的报错</p> 
<p style="color:black; margin-left:0; margin-right:0">https://gitee.com/dromara/liteFlow/issues/I4GY9L</p> 
<p style="color:black; margin-left:0; margin-right:0">修复 #I4FYKA jsonparser好像缺少脚本条件组件的解析</p> 
<p style="color:black; margin-left:0; margin-right:0">https://gitee.com/dromara/liteFlow/issues/I4FYKA</p> 
<p style="color:black; margin-left:0; margin-right:0">修复 #I4HQAA setIsEnd目前受isContinue的判断影响，还是会继续</p> 
<p style="color:black; margin-left:0; margin-right:0">https://gitee.com/dromara/liteFlow/issues/I4HQAA</p> 
<p style="color:black; margin-left:0; margin-right:0">修复 #I4HTY6 异步线程池不受配置控制的bug，一直是默认的数量</p> 
<p style="color:black; margin-left:0; margin-right:0">https://gitee.com/dromara/liteFlow/issues/I4HTY6</p> 
<h2 style="margin-left:30px; margin-right:30px"><span>五</span><span> </span></h2> 
<p style="color:black; margin-left:0; margin-right:0">不知不觉LiteFLow已经更新了26个版本了，目前已经1000 star左右。</p> 
<p style="color:black; margin-left:0; margin-right:0">你们的star和肯定是LiteFlow继续迭代的唯一动力。</p> 
<p style="color:black; margin-left:0; margin-right:0">我知道还有很多问题没解决好，也有槽点。LiteFlow从2020年开始全面开源，还很年轻，但请相信，在我们积极的迭代下，LiteFlow的后续形态会很好。</p> 
<p style="color:black; margin-left:0; margin-right:0">LiteFlow拥有一个很活跃技术氛围良好的社区群（不是开车的那种。。），如果你对此项目感兴趣，希望你能为项目点上star并加入社区。</p> 
<p style="color:black; margin-left:0; margin-right:0">具体加入方式：https://yomahub.com/liteflow/blog/group-chat</p> 
<p style="color:black; margin-left:0; margin-right:0">同时你支持这个项目的话，也欢迎赞助捐赠。每一个赞助捐赠者都会在官网记录以示感谢。</p> 
<p style="color:black; margin-left:0; margin-right:0">捐赠方式：https://yomahub.com/liteflow/blog/donation</p> 
<p><span style="color:#999999">- END -</span></p>
                                        </div>
                                      
</div>
            