
---
title: 'Netflix实用API设计1：Protobuf FieldMask实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://miro.medium.com/max/2000/1*Macl1dsyaNQQnVTKhh3Uag.png'
author: Dockone
comments: false
date: 2021-10-24 07:08:19
thumbnail: 'https://miro.medium.com/max/2000/1*Macl1dsyaNQQnVTKhh3Uag.png'
---

<div>   
<br><h2>背景</h2>在 Netflix，我们大量使用 <a href="https://grpc.io/">gRPC</a> 来实现后端到后端的通信。 当我们处理请求时，知道调用者对哪些字段感兴趣以及忽略哪些字段通常是有益的。 某些响应字段的计算成本可能很高，某些字段可能需要远程调用其他服务。 远程调用都是有代价的； 它们会带来额外的延迟，增加出错的可能性，并消耗网络带宽。 那么该如何知道响应中哪些字段不需要提供给调用者，从而避免进行不必要的计算以及远程调用？ 使用 GraphQL，这是通过使用字段选择器来实现的。 在 JSON:API 标准中，类似的技术称为<a href="https://jsonapi.org/format/#fetching-sparse-fieldsets">稀疏字段集</a>。 在设计 gRPC API 时，我们如何实现类似的功能？ 我们在 <a href="https://netflixtechblog.com/netflix-studio-engineering-overview-ed60afcfa0ce">Netflix Studio Engineering</a> 中使用的解决方案是 protobuf <a href="https://developers.google.com/protocol-buffers/docs/reference/csharp/class/google/protobuf/well-known-types/field-mask">FieldMask</a>。<br>
<br><h2>Protobuf FieldMask</h2><a href="https://developers.google.com/protocol-buffers">Protocol Buffers</a>，或简称为 protobuf，是一种数据序列化机制。 默认情况下，gRPC 使用 protobuf 作为其 IDL（接口定义语言）和数据序列化协议。<br>
FieldMask 是一个 protobuf 消息。 当此消息出现在 RPC 请求中时，有关如何使用此消息有许多实用工具（utilities）和约定。 FieldMask 消息包含一个名为paths 的字段，它用于指定字段，这些字段可以由读操作返回或由更新操作来修改。<br>
<br><pre class="prettyprint">message FieldMask &#123;<br>
// The set of field mask paths.<br>
repeated string paths = 1;<br>
</pre>&#125;<br>
<br><h2>案例: Netflix Studio Production</h2>假设有一个 Production 服务来管理 Studio Content Productions（在电影和电视行业中，术语<a href="https://en.wikipedia.org/wiki/Filmmaking">production</a>是指制作电影的过程，而不是运行软件的环境）。<br>
<br><pre class="prettyprint">// Contains Production-related information  <br>
message Production &#123;<br>
string id = 1;<br>
string title = 2;<br>
ProductionFormat format = 3;<br>
repeated ProductionScript scripts = 4;<br>
ProductionSchedule schedule = 5;<br>
// ... more fields<br>
&#125;<br>
<br>
service ProductionService &#123;<br>
// returns Production by ID<br>
rpc GetProduction (GetProductionRequest) returns (GetProductionResponse);<br>
&#125;<br>
<br>
message GetProductionRequest &#123;<br>
string production_id = 1;<br>
&#125;<br>
<br>
message GetProductionResponse &#123;<br>
Production production = 1;<br>
</pre>&#125;<br>
<br>GetProduction 通过唯一 ID 返回 Production 消息。 一个production包含多个字段，例如：标题、格式、日程安排日期、脚本又名剧本、预算、剧集等，但让我们保持这个例子简单，并在请求production时重点过滤日程安排日期和脚本。<br>
<br><h2>读取Production详细信息</h2>假设我们想要使用 GetProduction API 获取特定production的信息，例如“La Casa De Papel”。 虽然production有许多字段，但其中一些字段是从其他服务返回的，例如来自 Schedule 服务的 schedule 或来自 Script 服务的scripts。<br>
<br><img src="https://miro.medium.com/max/2000/1*Macl1dsyaNQQnVTKhh3Uag.png" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>每次调用 GetProduction 时，Production 服务都会向 Schedule 和 Script 服务发出 RPC，即使客户端忽略响应中的 schedule 和 scripts 字段。 如上所述，远程调用是有代价的。 如果服务知道哪些字段对调用者很重要，它可以在是否进行昂贵的调用、启动资源密集型计算和/或调用数据库这些事中做出明智的决定。 在这个例子中，如果调用者只需要标题和格式两个字段，Production 服务可以避免远程调用Schedule 和 Script 服务。<br>
<br>此外，请求大量字段会使响应负载变得庞大。 对某些应用程序来说可能是个问题，例如，在网络带宽有限的移动设备上。 在这些情况下，消费者只请求他们需要的字段是一种很好的做法。<br>
<br>一个比较笨的解决方法是添加额外的请求参数，例如 includeSchedule 和 includeScripts：<br>
<br><pre class="prettyprint">// Request with one-off "include" fields, not recommended<br>
message GetProductionRequest &#123;<br>
string production_id = 1;<br>
bool include_format = 2;<br>
bool include_schedule = 3;<br>
bool include_scripts = 4;<br>
</pre>&#125;<br>
<br>这种方法需要为每个昂贵的响应字段添加一个自定义的 includeXXX 字段，并且不适用于嵌套字段。 它还增加了请求的复杂性，最终使维护和支持更具挑战性。<br>
<br><h2>将 FieldMask 添加到请求消息中</h2>API 设计者可以将 field_mask 字段添加到请求消息中，而不是创建一次性的“包含”字段：<br>
<br><pre class="prettyprint">import "google/protobuf/field_mask.proto";<br>
<br>
message GetProductionRequest &#123;<br>
string production_id = 1;<br>
google.protobuf.FieldMask field_mask = 2;<br>
</pre>&#125;<br>
<br>消费者可以为他们希望在响应中收到的字段设置路径。 如果消费者只对标题和格式感兴趣，他们可以设置带有“title”和“format”路径的 FieldMask：<br>
<pre class="prettyprint">FieldMask fieldMask = FieldMask.newBuilder()<br>
.addPaths("title")<br>
.addPaths("format")<br>
.build();<br>
<br>
GetProductionRequest request = GetProductionRequest.newBuilder()<br>
.setProductionId(LA_CASA_DE_PAPEL_PRODUCTION_ID)<br>
.setFieldMask(fieldMask)<br>
.build();<br>
</pre><br>
<br><img src="https://miro.medium.com/max/2000/1*7cCe_kR8p6LafmTvOoFN9A.png" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>请注意，即使本博文中的代码示例是用 Java 编写的，演示的概念也适用于任何支持protocol buffers的其他语言。<br>
如果消费者只需要最后一个更新日程表的人的标题和电子邮件，他们可以设置不同的字段掩码：<br>
<pre class="prettyprint">FieldMask fieldMask = FieldMask.newBuilder()<br>
.addPaths("title")<br>
.addPaths("schedule.last_updated_by.email")<br>
.build();<br>
<br>
GetProductionRequest request = GetProductionRequest.newBuilder()<br>
.setProductionId(LA_CASA_DE_PAPEL_PRODUCTION_ID)<br>
.setFieldMask(fieldMask)<br>
.build();<br>
</pre><br>
<br>按照惯例，如果请求中不存在 FieldMask，则应返回所有字段。<br>
<br><h2>Protobuf 字段名称与字段编号</h2>你可能会注意到 FieldMask 中的路径是使用字段名称指定的，而在传输中，编码的protocol buffers消息仅包含字段编号，而不包含字段名称。 这（以及其他一些技术，如用于签名类型的 <a href="https://en.wikipedia.org/wiki/Variable-length_quantity#Zigzag_encoding">ZigZag</a> 编码）会让 protobuf 消息节省空间。<br>
<br>为了理解字段编号和字段名称之间的区别，让我们详细了解一下 protobuf 是如何编码和解码消息的。<br>
<br>我们的 protobuf 消息定义（.proto 文件）包含一个具有五个字段的 Production 消息。 每个字段都有一个类型、名称和编号。<br>
<br><pre class="prettyprint">// Message with Production-related information  <br>
message Production &#123;<br>
string id = 1;<br>
string title = 2;<br>
ProductionFormat format = 3;<br>
repeated ProductionScript scripts = 4;<br>
ProductionSchedule schedule = 5;<br>
</pre>&#125;<br>
<br>当 protobuf 编译器 (protoc) 编译此消息定义时，它会以你选择的语言（在我们的示例中为 Java）创建代码。 这个生成的代码包含定义消息的类，以及消息和字段描述符。 描述符包含将消息编码和解码为其二进制格式所需的所有信息。 例如，它们包含字段编号、名称、类型。 消息生产者使用描述符将消息转换为传输格式。 为提高效率，二进制消息仅包含字段数值对。 不包括字段名称。 当消费者收到消息时，它通过引用编译的消息定义将字节流解码为一个对象（例如，Java 对象）。<br>
<br><img src="https://miro.medium.com/max/2000/1*A64qBbKppk_KHqslo_PR2g.png" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>如上所述，FieldMask 列出字段名称，而不是数字。 在 Netflix，我们使用字段编号并使用 <a href="https://developers.google.com/protocol-buffers/docs/reference/java/com/google/protobuf/util/FieldMaskUtil.html#fromFieldNumbers-java.lang.Class-int...-">FieldMaskUtil.fromFieldNumbers()</a> 方法将它们转换为字段名称。 此方法利用编译的消息定义将字段编号转换为字段名称并创建 FieldMask。<br>
<pre class="prettyprint">FieldMask fieldMask = FieldMaskUtil.fromFieldNumbers(Production.class,<br>
Production.TITLE_FIELD_NUMBER,<br>
Production.FORMAT_FIELD_NUMBER);<br>
<br>
GetProductionRequest request = GetProductionRequest.newBuilder()<br>
.setProductionId(LA_CASA_DE_PAPEL_PRODUCTION_ID)<br>
.setFieldMask(fieldMask)<br>
.build();<br>
</pre><br>
<br>但是，有一个容易忽略的限制：使用 FieldMask 会限制你重命名消息字段的能力。 重命名消息字段通常被认为是一种安全操作，因为如上所述，字段名称不会被传输发送的，而是使用消费者端的字段编号派生的。 使用 FieldMask，字段名称会在消息负载中被发送出去（在路径字段值中）并且还是很重要的部分。<br>
<br>假设我们要将字段 title 重命名为 title_name 并发布消息定义的 2.0 版：<br>
<br><pre class="prettyprint">// version 2.0, with title field renamed to title_name<br>
message Production &#123;<br>
string id = 1;<br>
string title_name = 2;       // this field used to be "title"<br>
ProductionFormat format = 3;<br>
repeated ProductionScript scripts = 4;<br>
ProductionSchedule schedule = 5;<br>
</pre>&#125;<br>
<br><img src="https://miro.medium.com/max/2000/1*ZetuVXCnuSeREtzHzvAXJA.png" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>在此图表中，生产者（服务器）使用新的描述符，字段编号 2 名为 title_name。 传输发送的二进制消息包含字段编号及其值。 消费者仍然使用原始描述符，其中字段编号 2 作为标题。 它仍然能够通过字段号对消息进行解码。<br>
<br>如果消费者不使用 FieldMask 来请求字段，那倒是没问题。 如果消费者使用 FieldMask 字段中的“title”路径进行调用，生产者将无法找到该字段。 生产者在其描述符中没有名为 title 的字段，因此它不知道消费者请求的字段编号为 2。<br>
<br><img src="https://miro.medium.com/max/2000/1*FQgw3wWYqKJ9wjaiCClKRg.png" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>如我们所见，如果一个字段被重命名，后端应该能够支持新旧字段名称，直到所有调用者都迁移到新字段名称（向后兼容性问题）。<br>
<br>有多种方法可以处理此限制：<br>
- 使用 FieldMask 时切勿重命名字段。 这是最简单的解决方案，但并非总是可行<br>
- 要求后端支持所有旧的字段名称。 这解决了向后兼容性问题，但需要后端额外的代码来跟踪所有历史字段名称<br>
- 弃用旧字段并创建新字段而不是重命名。 在我们的示例中，我们将创建 title_name 字段编号 6。此选项比前- <br>
- 一个有一些优点：它允许生产者继续使用生成的描述符而不是自定义转换器； 此外，弃用一个字段在消费者端影响更大<br>
<br><pre class="prettyprint">message Production &#123;<br>
string id = 1;<br>
string title = 2 [deprecated = true];  // use "title_name" field instead<br>
ProductionFormat format = 3;<br>
repeated ProductionScript scripts = 4;<br>
ProductionSchedule schedule = 5;<br>
string title_name = 6;<br>
</pre>&#125;<br>
<br>无论采用哪种解决方案，重要的是要记住 FieldMask 使字段名称成为 API 合约中不可或缺的一部分。<br>
<br><h2>在生产者（服务器）端使用 FieldMask</h2>在生产者（服务器）端，可以使用 <a href="https://developers.google.com/protocol-buffers/docs/reference/java/com/google/protobuf/util/FieldMaskUtil.html#merge-com.google.protobuf.FieldMask-com.google.protobuf.Message-com.google.protobuf.Message.">FieldMaskUtil.merge()</a> 方法（8 和 9 行）从响应负载中删除不必要的字段：<br>
<br><pre class="prettyprint">@Override<br>
public void getProduction(GetProductionRequest request, <br>
                      StreamObserver<GetProductionResponse> response) &#123;<br>
<br>
Production production = fetchProduction(request.getProductionId());<br>
FieldMask fieldMask = request.getFieldMask();<br>
<br>
Production.Builder productionWithMaskedFields = Production.newBuilder();<br>
FieldMaskUtil.merge(fieldMask, production, productionWithMaskedFields);<br>
<br>
GetProductionResponse response = GetProductionResponse.newBuilder()<br>
    .setProduction(productionWithMaskedFields).build();<br>
responseObserver.onNext(response);<br>
responseObserver.onCompleted();<br>
</pre>&#125;<br>
<br>如果服务端代码还需要知道请求哪些字段以避免进行外部调用、数据库查询或昂贵的计算，则可以从 FieldMask 路径字段中获取此信息：<br>
<br><pre class="prettyprint">private static final String FIELD_SEPARATOR_REGEX = "\\.";<br>
private static final String MAX_FIELD_NESTING = 2;<br>
private static final String SCHEDULE_FIELD_NAME =                                // (1)<br>
Production.getDescriptor()<br>
.findFieldByNumber(Production.SCHEDULE_FIELD_NUMBER).getName();<br>
<br>
@Override<br>
public void getProduction(GetProductionRequest request, <br>
                      StreamObserver<GetProductionResponse> response) &#123;<br>
<br>
FieldMask canonicalFieldMask =                                               <br>
    FieldMaskUtil.normalize(request.getFieldMask());                         // (2) <br>
<br>
boolean scheduleFieldRequested =                                             // (3)<br>
    canonicalFieldMask.getPathsList().stream()<br>
        .map(path -> path.split(FIELD_SEPARATOR_REGEX, MAX_FIELD_NESTING)[0])<br>
        .anyMatch(SCHEDULE_FIELD_NAME::equals);<br>
<br>
if (scheduleFieldRequested) &#123;<br>
    ProductionSchedule schedule = <br>
        makeExpensiveCallToScheduleService(request.getProductionId());       // (4)<br>
    ...<br>
&#125;<br>
<br>
...<br>
</pre>&#125;<br>
<br>此代码仅在schedule 字段被请求时调用 makeExpensiveCallToScheduleService 方法（第 21 行）。 让我们更详细地探索这个代码示例。<br>
<br>(1) SCHEDULE_FIELD_NAME 常量包含字段的名称。 此代码示例使用消息类型 <a href="https://developers.google.com/protocol-buffers/docs/reference/java/com/google/protobuf/Descriptors">Descriptor</a> 和 <a href="https://developers.google.com/protocol-buffers/docs/reference/java/com/google/protobuf/Descriptors.FieldDescriptor.html">FieldDescriptor</a> 通过字段编号查找字段名称。 protobuf 字段名称和字段编号之间的区别在上面的 Protobuf 字段名称与字段编号部分进行了描述。<br>
<br>(2) <a href="https://developers.google.com/protocol-buffers/docs/reference/java/com/google/protobuf/util/FieldMaskUtil.html#normalize-com.google.protobuf.">FieldMaskUtil.normalize()</a> 返回具有按字母顺序排序和去重的字段路径（又名规范形式）的 FieldMask。<br>
<br>(3) scheduleFieldRequestedvalue 表达式（第14 - 17 行）采用 FieldMask 路径流，将其映射到顶级（top-level）字段流，如果顶级字段包含 SCHEDULE_FIELD_NAME 常量的值，则返回 true。<br>
<br>(4) 仅当 scheduleFieldRequested 为真时才检索 ProductionSchedule。<br>
<br>如果你决定将 FieldMask 用于不同的消息和字段，请考虑创建可重用的实用封装方法。 例如，基于 FieldMask 和 FieldDescriptor 返回所有顶级字段的方法，如果字段存在于 FieldMask 中则返回的方法等。<br>
<br><h2>发布预编译的 FieldMask</h2>某些访问模式可能比其他访问模式更常见。 如果多个消费者对同一字段子集感兴趣，API 生产者可以提供带有 FieldMask 的客户端库，用于最常用的字段组合。<br>
<br><pre class="prettyprint">public class ProductionFieldMasks &#123;<br>
/**<br>
 * Can be used in &#123;@link GetProductionRequest&#125; to query <br>
 * production title and format<br>
 */<br>
public static final FieldMask TITLE_AND_FORMAT_FIELD_MASK = <br>
    FieldMaskUtil.fromFieldNumbers(Production.class,<br>
        Production.TITLE_FIELD_NUMBER, Production.FORMAT_FIELD_NUMBER);<br>
<br>
/**<br>
 * Can be used in &#123;@link GetProductionRequest&#125; to query <br>
 * production title and schedule<br>
 */<br>
public static final FieldMask TITLE_AND_SCHEDULE_FIELD_MASK = <br>
    FieldMaskUtil.fromFieldNumbers(Production.class,<br>
        Production.TITLE_FIELD_NUMBER, <br>
        Production.SCHEDULE_FIELD_NUMBER);<br>
<br>
/**<br>
 * Can be used in &#123;@link GetProductionRequest&#125; to query <br>
 * production title and scripts<br>
 */<br>
public static final FieldMask TITLE_AND_SCRIPTS_FIELD_MASK = <br>
    FieldMaskUtil.fromFieldNumbers(Production.class,<br>
        Production.TITLE_FIELD_NUMBER, Production.SCRIPTS_FIELD_NUMBER);<br>
</pre>&#125;<br>
<br>提供预编译的字段掩码可以简化最常见场景的 API 使用，并使消费者能够灵活地为更具体的用例构建自己的字段掩码。<br>
<br><h2>限制</h2>- 使用 FieldMask 会限制重命名消息字段的能力（在 Protobuf 字段名称与字段编号部分中描述）<br>
- 重复字段只允许出现在路径字符串的最后一个位置。 这意味着你不能在列表内的消息中选择（屏蔽）单个子字段。 这在可预见的未来可能会发生变化，因为最近批准的 Google API 改进提案 AIP-161 字段掩码包括对重复字段的通配符的支持。<br>
<br><h2>总结</h2>Protobuf FieldMask 是一个简单但功能强大的概念。 它可以帮助使 API 更健壮，服务实现更高效。<br>
这篇博文介绍了 Netflix Studio Engineering 如何以及为何将其用于读取数据的 API。 <a href="https://netflixtechblog.com/practical-api-design-at-netflix-part-2-protobuf-fieldmask-for-mutation-operations-2e75e1d230e4">第 2 部分</a>将阐明使用 FieldMask 进行更新和删除操作。<br>
<br>原文链接：<a href="https://netflixtechblog.com/practical-api-design-at-netflix-part-1-using-protobuf-fieldmask-35cfdc606518">Practical API Design at Netflix, Part 1: Using Protobuf FieldMask</a>（翻译：王欢）
                                
                                                              
</div>
            