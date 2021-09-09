
---
title: 'OpenSSL 3.0 正式发布，更改许可协议并弃用所有低级别 API'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5785'
author: 开源中国
comments: false
date: Thu, 09 Sep 2021 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5785'
---

<div>   
<div class="content">
                                                                                            <p>经过 3 年的开发，17 个 alpha 版本，2 个 beta 版本，超过 7500 个提交，以及来自 350 位不同开发者的贡献，OpenSSL 3.0 终于正式发布了。</p> 
<h3><strong>OpenSSL 1.1.1 以来的主要变化</strong></h3> 
<ul> 
 <li> <p><strong>主要版本</strong></p> <p>开发者可以从<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssl.org%2Fsource%2F" target="_blank">这里下载</a> OpenSSL 3.0，并升级你的应用程序使之兼容。OpenSSL 3.0 是一个大版本升级，并不完全向后兼容以前的版本。大多数使用 OpenSSL 1.1.1 的应用程序仍然可以正常工作，只是需要重新编译（可能会有关于使用废弃的 API 的编译警告）。还有一些不能完全兼容的应用可能需要进行修改才能正确编译和使用。</p> <p>如果应用程序需要利用 OpenSSL 3.0 中的一些新功能（例如 FIPS 模块），也需要对应用进行更改。</p> </li> 
 <li> <p><strong>许可证变更</strong></p> <p>在以前的版本中，OpenSSL 是在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssl.org%2Fsource%2Flicense-openssl-ssleay.txt" target="_blank">OpenSSL 和 SSLeay</a> 下获得<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssl.org%2Fsource%2Flicense-openssl-ssleay.txt" target="_blank">许可的</a>。从 OpenSSL 3.0 开始，已经过渡到了 Apache License 2.0。旧的 OpenSSL 和 SSLeay 许可证仍然适用于旧版本（1.1.1 和更早的版本）。</p> </li> 
 <li> <p><strong>Providers 和 FIPS 支持</strong></p> <p>OpenSSL 1.1.1 的主要变化之一是引入了 Providers（提供者） 概念。<strong>Providers</strong> 聚集在一起并提供可用的算法实现。使用 OpenSSL 3.0，可以以编程方式或通过配置文件指定你希望用于任何给定应用程序的 Providers。OpenSSL 3.0 标配 5 个不同的 Providers。随着时间的推移，第三方可能会分发可以接入 OpenSSL 的其他 Providers。通过 Providers 提供的所有算法实现都可以通过“高级” API 访问，无法使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssl.org%2Fdocs%2Fman3.0%2Fman7%2Fmigration_guide.html%23Low-Level-APIs" target="_blank">“低级 API”</a> 访问它们。</p> <p>目前可用的一个标准 Providers 是 FIPS Providers。这使得 FIPS 验证的加密算法可用。FIPS Providers 默认处于禁用状态，需要在配置时使用<code>enable-fips</code>选项显式启用。如果启用，除了其他标准 Providers 之外，还会构建和安装 FIPS Providers，不需要单独的安装过程。</p> </li> 
 <li> <p><strong>低级别的 API</strong></p> <p>OpenSSL 历来提供两套用于调用加密算法的 API："高级" API（如 <code>EVP</code> API）和 "低级" API。高级别的 API 通常被设计成适用于所有算法类型。而 "低级" API 则是针对特定的算法实现的。长期以来，OpenSSL 开发团队一直不鼓励使用低级别的 API。在 OpenSSL 3.0 中，这一点变得更加明确。所有这些低级别的 API 都已经被废弃了。你仍然可以在你的应用程序中使用它们，但你可能会在编译过程中开始看到弃用警告。废弃的 API 可能会从未来的 OpenSSL 版本中删除，所以强烈建议开发者更新你的代码，以使用高级 API 来代替。</p> </li> 
 <li> <p><strong>版本管理</strong></p> <p>OpenSSL 的版本管理已经随着 OpenSSL 3.0 的发布而改变，新的版本管理采用下方这样的格式：</p> <p>MAJOR.MINOR.PATCH（主版本.次版本.补丁）</p> <p>对于 OpenSSL 1.1.1 及以下版本，不同的补丁级别是由版本号后面的字母表示的，这一方法将不再使用，而是用版本号中的最后一个数字来表示补丁级别。第二个数字（MINOR）的变化表明可能已经添加了新的功能，但与相同 MAJOR 编号的 OpenSSL 在 API 和 ABI 上是兼容的。如果 MAJOR 数字发生变化，则不保证 API 和 ABI 的兼容性。</p> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssl.org%2Fdocs%2Fman3.0%2Fman7%2Fmigration_guide.html" target="_blank">https://www.openssl.org/docs/man3.0/man7/migration_guide.html</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            