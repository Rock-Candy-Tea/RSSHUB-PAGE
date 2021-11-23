
---
title: 'Julia 编程语言 v1.6.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6409'
author: 开源中国
comments: false
date: Tue, 23 Nov 2021 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6409'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Julia 1.6.4 版本是 1.6 系列中的第四个补丁版本，现已正式发布。作为一个补丁版本，1.6.4 版本不包含新的功能或重大变化，只包含错误修复、文档改进和性能改进。</p> 
<p>Julia 1.6.4 的更新内容包括：</p> 
<ul> 
 <li>修复 Buildkite 上的<code>cmdlineargs</code> 测试 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F42118" target="_blank">#42118</a></li> 
 <li><code>Base.julia_cmd()</code>：正确转发<code>-sysimage-native-code=no</code>标志（如果提供） <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F42185" target="_blank">#42185</a></li> 
 <li>CI（Buildkite，代码覆盖率）：增加 <code>JULIA_WORKER_TIMEOUT</code> 在代码覆盖率作业的值 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F42193" target="_blank">#42193</a></li> 
 <li>CI（Buildkite，代码覆盖率）：如果覆盖率低得令人怀疑，则表明在覆盖率工作的早期出现了问题，因此代码覆盖率作业失败 #42213</li> 
 <li>CI（Buildkite、GHA）：允许任何具有分类或提交权限的用户重试所有失败的 Buildkite 作业 #42138</li> 
 <li>CI (Buildkite)：在实验性<code>asan</code>作业中，删除 “Test that ASAN is enabled” 步骤，但保留 “Build julia-debug with ASAN” 步骤 #42229</li> 
 <li>稍微放宽测试，以便在使用 MKL 时通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F42315" target="_blank">linalg</a> 测试 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F42315" target="_blank">#42315</a></li> 
 <li>CI (GHA)：在拉取请求被打开或同步时才运行<code>Statuses</code>工作流 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F42389" target="_blank">#42389</a></li> 
 <li>CI (GHA)：更新到<code>retry-buildkite action</code>的最新提交 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F42386" target="_blank">#42386</a></li> 
 <li>修补 Openblas v0.3.10 以修复 EXCEPTION_ACCESS_VIOLATION <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F42397" target="_blank">#42397</a></li> 
 <li>codegen: 修复空元组的 unswitchtupleunion</li> 
 <li>解决注册表损坏问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F41934" target="_blank">#41934</a></li> 
 <li>CI (Buildkite)：为更多 Linux 架构添加<code>package_linux</code>和<code>tester_linux</code><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F41707" target="_blank">#41707</a></li> 
 <li>修复验证器以允许 GlobalRef 作为赋值 RHS <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F42417" target="_blank">#42417</a></li> 
 <li>改进 apply_type 错误消息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F42422" target="_blank">#42422</a></li> 
 <li>CI (Buildkite)：显式设置<code>OPENBLAS_NUM_THREADS</code>环境变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F42470" target="_blank">#42470</a></li> 
 <li>CI（Buildkite）：在 Buildkite 缓存中，不要缓存默认 depot 中的 “registries” 目录 #42475</li> 
 <li>CI (Buildkite): 添加 <code>package_musl64</code> 和 <code>tester_musl64</code>  #42476</li> 
 <li>在启用多线程时改进分布式测试套件中的一些测试 #42499</li> 
 <li>CI (buildkite)：确保在传递 <code>-j</code> 时传递 <code>--output-sync</code> #42511</li> 
 <li>CI (Buildkite)：删除一个空的 YAML 文件 #42531</li> 
 <li>CI (Buildkite)：重新组织<code>tester_linux.yml</code>文件中的一些逻辑 #42514</li> 
 <li>添加允许<code>stale_cachefile</code>忽略加载模块的选项 #42545</li> 
 <li>修复 libgit2 错误抛出 #42576</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fcompare%2Fv1.6.3...v1.6.4" target="_blank">https://github.com/JuliaLang/julia/compare/v1.6.3...v1.6.4</a></p>
                                        </div>
                                      
</div>
            