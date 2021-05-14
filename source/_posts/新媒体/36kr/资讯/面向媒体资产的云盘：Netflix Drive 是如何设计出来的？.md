
---
title: '面向媒体资产的云盘：Netflix Drive 是如何设计出来的？'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210513/v2_e6ff18730bb34e48ac2f9156a05ca0c1_img_jpg'
author: 36kr
comments: false
date: Fri, 14 May 2021 02:47:43 GMT
thumbnail: 'https://img.36krcdn.com/20210513/v2_e6ff18730bb34e48ac2f9156a05ca0c1_img_jpg'
---

<div>   
<blockquote> 
 <p>神译局是36氪旗下编译团队，关注科技、商业、职场、生活等领域，重点介绍国外的新技术、新观点、新风向。</p> 
</blockquote> 
<p>编者按：Netflix已经从最初的视频点播和DVD租赁服务公司变成了现在的流媒体平台巨头，并且在原<a class="project-link" data-id="216918" data-name="创方" data-logo="https://img.36krcdn.com/20201112/v2_14360b733f7547f58772a6a96ad82d93_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/216918" target="_blank">创方</a>面的投入也越来越大。为了支撑众多创作人员的分布式协作，Netflix在内部也开发了不少出色的技术。而且鉴于公司出色的企业文化，他们总是乐于将自己的技术实现分享出来。针对旗下艺术家跨地区、跨项目在受控下访问不同的媒体资产的需求，他们开发了自己的网盘：Netflix Drive。最近，在他们的官方博客上，Netflix把Netflix Drive的技术架构和设计思路公布了出来，感兴趣的可以参考一下。原文标题是：<em>Netflix Drive</em>。</p> 
<p class="image-wrapper"><img data-img-size-val="960,600" src="https://img.36krcdn.com/20210513/v2_e6ff18730bb34e48ac2f9156a05ca0c1_img_jpg" referrerpolicy="no-referrer"></p> 
<p>在本文中，我们将介绍Netflix Drive，一种为媒体资产准备的云盘，并对部分功能和接口提供高层概述。我们打算把本文作为覆盖Netflix Drive的系列文章的第一篇。在之后的系列文章中，我们将对Netflix Drive的若干组件进行架构性的深入研究。</p> 
<p>Netflix，尤其是Studio应用（以及云端的Studio）产生的数据高达数PB，其中就包含有价值数十亿美元的媒体资产。我们的艺术家和工作流可能会分布在全球各地，从事不同的项目，而每一个项目产生的内容都构成了一个大型的资产库的一部分。</p> 
<p>下图就是遍布全球的分布式制作的一个例子，不同的艺术家和工作流共同协作，创建出一个或多个项目的资产并进行共享。</p> 
<p class="image-wrapper"><img data-img-size-val="1346,748" src="https://img.36krcdn.com/20210513/v2_83120298226f4848a014557b23bcfebb_img_png" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图1：跨越全球的分布式制作，来自世界各地的艺术家要制作不同的资产</p> 
<p>在有些工作流当中，艺术家可能希望能浏览大型数据集当中的部分资产子集，比方说，跟特定项目有关的子集。这些艺术家可能想要创建个人工作区，并开展临时性资产的制作工作。为了支持此类用例，向这些艺术家呈现相关数据全局一致的视图，就必须支持用户工作区和项目工作区级别的访问控制。</p> 
<p>Netflix Drive旨在解决以下问题：暴露不同的名称空间，添加适当的访问控制，从而帮助构建高性能，可扩展，全球分布的平台来存储和检索相关资产。</p> 
<blockquote> 
 <p>我们对Netflix Drive的设想是作为Studio和Media应用的Cloud Drive（云盘），并让它成为访问Netflix所有内容的通用解决方案。</p> 
</blockquote> 
<p>它对应用开发了一个文件/文件夹接口，用来保存数据，并为控制操作提供了一个API接口。Netflix Drive依赖于一个将会资产的持久存储层的数据存储，以及一个元数据存储，这个元数据存储将会提供从文件系统层次结构到数据存储实体的相关映射。如图2所示，主体部分是文件系统接口，API接口，元数据以及数据存储。我们会在以下各节对此分别进行深入研究。</p> 
<p class="image-wrapper"><img data-img-size-val="1874,1150" src="https://img.36krcdn.com/20210513/v2_058797e0ec9b4748974e15cc21e9421d_img_png" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图2：Netflix Drive的组件</p> 
<p> </p> 
<h3>Netflix Drive的文件接口</h3> 
<p>Nuke，Maya，Adobe Photoshop等创意应用利用文件和文件夹来存储和检索内容。Netflix Drive则要靠FUSE（用户空间的文件系统，File System In User Space），提供连接此类的应用的POSIX文件和文件夹接口。基于FUSE的POSIX接口可提供自定义功能的弹性，部署配置的灵活性以及标准及无缝的文件/文件夹接口。Windows（WinFSP ）和MacOS （MacFUSE）都有类似的用户空间抽象。</p> 
<p>源自用户、应用以及系统动作对文件和文件夹的操作，会被转换为一组定义明确的功能和系统调用，由Linux虚拟文件系统层（或Windows的透传/过滤驱动）转发给用户空间的FUSE层。所产生的元数据和数据操作则交由Netflix Drive适当的元数据和数据适配器实现。</p> 
<p class="image-wrapper"><img data-img-size-val="1828,874" src="https://img.36krcdn.com/20210513/v2_4a491b4674df4b4db3a543e2f4877100_img_png" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图3：Netflix Drive的POSIX接口</p> 
<p>Netflix Drive的POSIX文件和文件夹接口被设计为分层系统，顶层是FUSE实现钩子。这一层会为要实现的所有相关VFS调用提供入口点。Netflix Drive在FUSE之下还有一个抽象层，这一层可以让不同的元数据和数据存储通过让相应的适配器实现接口而插入到该体系结构内。我们会在下面的部分进一步讨论有关分层体系结构的更多信息。</p> 
<h3>Netflix Drive的API接口</h3> 
<p>除了公开一个将会成为所有抽象的中心的文件接口外，Netflix Drive还开放了API和Polled Task接口，让应用和工作流工具可以触发Netflix Drive的控制操作。</p> 
<p>例如，应用可以显式利用REST端点把存储在Netflix Drive里面的文件发布到云端，然后再用REST端点通过云端检索已发布文件的子集。API接口还可用于跟踪大文件的传输，并允许其他应用基于Netflix Drive进行开发。</p> 
<p class="image-wrapper"><img data-img-size-val="1496,1160" src="https://img.36krcdn.com/20210513/v2_b18852b1d4f546b39516e6baa9c651c1_img_png" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图4：Netflix Drive的控制接口</p> 
<p>Polled Task接口可让studio和media工作流程编排器发布或分派任务给不同的工作站或容器上的Netflix Drive实例。这可以在工作站启动时让Netflix Drive以空的命名空间启动，并动态映射跟艺术家概念设计过程或者工作流阶段相关的一组资产。此外，这些资产还可以映射到艺术家或应用选定的名称空间里面。</p> 
<p>或者，工作站/容器启动的时候可以加载预取的用户感兴趣的资产。这可以让艺术家和应用获取一个已经包含有相关文件的工作站，并可以选择在设计过程期间对资产树进行添加和删除。比方说，艺术家对文件执行转换工作，并利用Netflix Drive来存储/获取中间结果以及最终的副本，后者则可以转换成媒体资产。</p> 
<h3>Netflix Drive的引导</h3> 
<p>鉴于应用跟Netflix Drive的交互可以有两种不同模式，现在就让我们来讨论一下如何引导Netflix Drive。</p> 
<p>在启动时，Netflix Drive需要一份清单，这份清单应该包含有关数据存储，元数据存储以及（与用户登录相关的）凭据的信息，这样才能形成命名空间层次结构的实例。Netflix Drive的挂载点可以包含有多个Netflix Drive名称空间。</p> 
<p>动态实例使得Netflix Drive可以显示用户选择且可访问的来自大型资产库的数据子集。用户实例让它可以像Cloud Drive一样工作，而用户对内容的处理会在后台定期自动同步到云端。当用户在新的计算机上重新启动时，同样的文件和文件夹会从云端预取下来。在后续的博客文章中，我们会更详细地介绍Netflix Drive的不同命名空间。</p> 
<p>下面是一个典型的引导清单文件的例子。</p> 
<p class="image-wrapper"><img data-img-size-val="1074,1432" src="https://img.36krcdn.com/20210513/v2_c89c7c52f6ec4bfa9ed09743b879a96c_img_png" referrerpolicy="no-referrer"></p> 
<p class="img-desc">清单文件例子：此图显示的是引导清单json文件，从中可以看出Netflix Drive是怎么跟不同的元数据存储（如Redis、CockroachDB ）和数据存储（如Ceph、S3）配合使用，并将它们捆绑在一起来提供资产的持久层的</p> 
<p>清单是让用户工作站具备Netflix Drive个性的持久性工件。它不受实例故障影响，而且可以在任何新部署的实例上重新创建相同的有状态接口。</p> 
<h3>元数据与数据存储抽象</h3> 
<p>为了让各种不同的元数据存储和数据存储可以轻松地植入到这个体系结构里面，Netflix Drive还开放了元数据和数据存储的抽象接口。下图是解释Netflix Drive不同抽象层的图解</p> 
<p class="image-wrapper"><img data-img-size-val="1272,924" src="https://img.36krcdn.com/20210513/v2_437f0880d9cd4778bfb63377511f94d4_img_png" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图5：Netflix Drive的分层体系结构</p> 
<h4>元数据存储的特征</h4> 
<p>Netflix Drive里面的每个文件都会有一个或多个对应的元数据节点，分别对应文件的不同版本。文件系统层次结构会被建模成元数据存储里面的一颗树，根节点将是应用的顶层文件夹。</p> 
<p>每个元数据节点会包含有若干属性，比如文件的校验和数据的位置，用户访问数据的权限，文件元数据（比如大小，修改时间等）。元数据节点还可以提供对扩展属性的支持，这些属性可以用来对ACL，符号链接或其他表现性文件系统建构进行建模。</p> 
<p>元数据存储区还可以揭示工作区的概念，也就是每个用户/应用可以有多个工作空间，而且可以跟其他用户/应用共享工作区。这些更高级别的建构对Studio应用非常有用。</p> 
<h4>数据存储的特征</h4> 
<p>Netflix Drive的实现离不开数据存储。这种数据存储可以把字节流变成放在存储介质里面的持久存储的文件/对象。数据存储应开放API，让Netflix Drive执行I / O操作。字节传输的传输机制是数据存储的一项功能。</p> 
<p>在第一份清单里面，Netflix Drive利用了一个对象存储（比如Amazon S3）作为数据存储。为了公开类似文件存储的属性，对象存储中需要进行一些更改。每个文件可以存储为一个或多个对象。对于Studio应用来说，文件大小有可能会超过Cloud Storage最大的对象大小，因此，数据存储服务应具有将文件的多个部分存储为单独对象的能力。数据存储服务负责把这些对象绑定到一个文件，并把这些对象的唯一ID通知给元数据存储。数据存储在内部实现了把文件分割成若干部分，对内容进行加密以及对数据进行生命周期管理等功能。</p> 
<h4>多层架构</h4> 
<p>Netflix Drive通过其引导清单让多个数据存储成为同一安装的一部分。</p> 
<p class="image-wrapper"><img data-img-size-val="1508,1236" src="https://img.36krcdn.com/20210513/v2_11be4ebd1e5a448b804097c5a6ba9f3e_img_png" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图6：Netflix Drive的多个数据存储</p> 
<p>某些工作室应用（比如编码和代码转换）的I/O特征跟典型的云盘不一样。</p> 
<p>这些应用生成的大多数数据在本质上都是临时性的，而且一开始读取会非常频繁。最终的编码副本需要保留，而临时数据则可以删除。为了服务于此类应用，Netflix Drive可以把临时数据持久化存储到距离应用较近的存储层，从而降低读取时延，并提高读取请求的经济性，因为云存储读取会产生出口成本。最后，一旦编码后的副本准备就绪，就可以由Netflix Drive持久保存到云端的持久存储层。单个数据存储也可以选择将存储在更廉价的替代物里面的内容子集归档。</p> 
<h3>安全</h3> 
<p>Studio应用要求严格遵守安全模型，只有具备特定权限的用户或应用才可以访问特定资产。安全性是Netflix Drive设计的基石之一。Netflix Drive动态命名空间设计可让艺术家或工作流根据工作区信息和访问控制仅访问资产的一小部分，这是在Studio工作流里面用Netflix Drive的好处之一。Netflix Drive把身份验证和授权模型封装到元数据存储里面。这些会被转换为Netflix Drive里面的POSIX ACL。将来，Netflix Drive可以通过利用跟资产对应的元数据节点关联的扩展属性来支持更具表现性的ACL。</p> 
<p>Netflix Drive目前已被多支Studio团队用作资产的铺路解决方案，而且也跟多个媒体套件应用集成。从今天起，Netflix Drive可以安装在CentOS，MacOS和Windows上。在未来的博客文章里，我们会介绍Netflix Drive的实现细节，相关知识，性能分析以及基于Netflix Drive开发的部分应用和工作流。</p> 
<p>译者：boxi</p>  
</div>
            