
---
title: 'Arthas 发布 3.5.5 版本，支持 macOS ARM64 架构，改进易用性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://arthas.aliyun.com/doc/_images/arthas.png'
author: 开源中国
comments: false
date: Wed, 08 Dec 2021 15:21:00 GMT
thumbnail: 'https://arthas.aliyun.com/doc/_images/arthas.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt src="https://arthas.aliyun.com/doc/_images/arthas.png" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><code>Arthas</code>是Alibaba开源的Java诊断工具，深受开发者喜爱。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>Github：https://github.com/alibaba/arthas</p> </li> 
 <li> <p>文档：https://arthas.aliyun.com/doc/</p> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">Arthas 最新发布了 3.5.5 版本，主要支持macOS ARM64架构，以及改进易用性。</p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:justify">vmtool 命令支持macOS ARM64架构</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">目前<code>vmtool</code>的动态库文件是由github action构建的。但github action还不支持mac M1环境，所以<code>vmtool</code>命令之前没支持mac M1机器。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">但通过交叉编译的方式，在使用clang编译时指定多个arch就可以生成所谓的<code>Fat Library</code>，即在一个文件里同时支持多种架构。</p> 
<pre style="margin-left:0; margin-right:0; text-align:justify"><code>-arch x86_64 -arch arm64
</code></pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">使用<code>file</code>命令可以查看<code>vmtool</code>使用的<code>dylib</code>已经同时支持<code>x86_64</code>和<code>arm64</code>：</p> 
<pre style="margin-left:0; margin-right:0; text-align:justify"><code>$ file lib/libArthasJniLibrary.dylib
lib/libArthasJniLibrary.dylib: Mach-O universal binary with 2 architectures: [x86_64:Mach-O 64-bit dynamically linked shared library x86_64] [arm64:Mach-O 64-bit dynamically linked shared library arm64]
lib/libArthasJniLibrary.dylib (for architecture x86_64):Mach-O 64-bit dynamically linked shared library x86_64
lib/libArthasJniLibrary.dylib (for architecture arm64):Mach-O 64-bit dynamically linked shared library arm64
</code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:justify">async-profiler 升级到2.5版本，生成html结果支持查找，支持macOS ARM64架构</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">升级到2.5版本后，<code>profiler</code>命令只支持生成<code>html</code>格式结果，不再支持<code>svg</code>格式了。<code>html</code>格式可以更好的查找过滤。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">比如在查找<code>File</code>关键字之后，可以看到<code>紫色</code>的高亮结果：</p> 
<p><img height="601" src="https://oscimg.oschina.net/oscnet/up-d6d77340bae575c19515b323c84dc0cb545.png" width="1080" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:justify">WebConsole支持配置向上回滚行数</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">目前WebConsole默认只支持向上回滚1000行，但有的命令输出结果很长，之前的结果就会被覆盖掉。因此增加<code>scrollback</code>参数，用户可以自定义配置。比如</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>http://localhost:8563/?scrollback=2000</p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:justify">改进低版本JDK attach高版本JDK支持</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">在使用低版本JDK attach高版本JDK 进程时，可能会抛出异常<code>IOException: Non-numeric value found - int expected</code>，但实际上已经attach成功。这对用户会造成困扰。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">因此改进为打印提示，但仍然会成功连接，用户可以直接诊断。</p> 
<p><img height="662" src="https://oscimg.oschina.net/oscnet/up-1943d5793535e84e1441dece5920e6e7f94.png" width="1080" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:justify">总结</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>profiler wiki: https://arthas.aliyun.com/doc/jad.html</p> </li> 
 <li> <p>Release 日志: https://github.com/alibaba/arthas/releases/tag/arthas-all-3.5.5</p> </li> 
</ul> 
<p><a href="https://www.oschina.net/project/top_cn_2021?id=52">2021中国开源项目评选，请投Arthas一票！</a></p>
                                        </div>
                                      
</div>
            