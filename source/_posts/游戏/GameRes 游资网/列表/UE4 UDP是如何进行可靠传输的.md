
---
title: 'UE4 UDP是如何进行可靠传输的'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202105/18/130708d2jmbzbfzgxv0vxx.png'
author: GameRes 游资网
comments: false
date: Tue, 18 May 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202105/18/130708d2jmbzbfzgxv0vxx.png'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2497156">
TCP 和 UDP 都是具有代表性的传输层协议，很多时候我们都会拿它们做比较，区别如下：<br>
<br>
<div align="center">
<img id="aimg_979047" aid="979047" zoomfile="https://di.gameres.com/attachment/forum/202105/18/130708d2jmbzbfzgxv0vxx.png" data-original="https://di.gameres.com/attachment/forum/202105/18/130708d2jmbzbfzgxv0vxx.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/18/130708d2jmbzbfzgxv0vxx.png" referrerpolicy="no-referrer">
</div><br>
<strong>对它们的工作方式打个比喻：</strong><br>
<br>
TCP 就好比打电话，通话之前先拨通电话，通了之后互相对话，信号不好的时候还是会询问“喂喂喂？“、”你那边能听到吗？“之类的确认对方能听到才继续通话，结束之后 say bye bye。<br>
<br>
UDP 就好比寄信，提前把想说的全写信里，之后寄出去，然后就结束了。不清楚有没有到对方手里，也不清楚对方有没有回信。<br>
<br>
UDP 想要实现可靠性传输，通常的做法是在应用层模拟 TCP 的可靠性传输。比如<br>
<br>
<ul><li>添加发送和接收缓冲区</li><li>添加序列号和应答</li><li>添加超时重传，丢包重传</li><li>添加流量控制<br>
</li></ul><br>
理论归理论，具体的实现又是怎样的呢？小小的脑袋的我打开了 UE4 的源码。。。<br>
<br>
目录<br>
<br>
<ul><li>前言</li><li>UE4</li><li>网络框架</li><li>NetDrivers, NetConnections, and Channels</li><li>Initiating Connections / Handshaking Flow</li><li>重新建立丢失的连接</li><li>数据传输</li><li>可靠性和重传</li><li>网络框架图</li><li>源码分析</li><li>基本概念</li><li>消息的发送</li><li>消息的接收</li><li>流量控制</li><li>总结<br>
</li></ul><br>
<br>
<strong><font color="#de5650">UE4</font></strong><br>
<br>
<strong><font color="#de5650">网络框架</font></strong><br>
<br>
NetDrivers, NetConnections, and Channels<br>
<br>
<strong>UNetDrivers</strong><br>
<br>
网络驱动，网络处理的核心，负责管理 UNetConnections，以及它们之间可以共享的数据。对于某个游戏来说，一般会有相对较少的 UNetDrivers，这些可能包括：<br>
<br>
1、Game NetDriver：负责标准游戏网络流量<br>
<br>
2、Demo NetDriver：负责录制或回放先前录制的游戏数据，这就是重播（观战）的工作原理。<br>
<br>
3、Beacon NetDriver：负责不属于“正常”游戏流量的网络流量。<br>
<br>
当然，也可以自定义 NetDrivers，由游戏或应用程序实现并使用。<br>
<br>
<strong>NetConnections</strong><br>
<br>
表示连接到游戏（或更一般的说，连接到 NetDriver）的单个客户端。每个网络连接都有自己的一组通道，连接将数据路由到通道。<br>
<br>
<strong>Channel</strong><br>
<br>
数据通道，每一个通道只负责交换某一个特定类型特定实例的数据信息。<br>
<br>
1、Control Channel：用于发送有关连接状态的信息（连接是否应该关闭等）。<br>
<br>
2、Voice Channel：用于在客户端和服务器之间发送语音数据。<br>
<br>
3、Actor Channel：从服务器复制到客户端的每个 Actor 都将存在唯一的 Actor 通道。（Actor 是在世界中存在的对象，UE4 大部分的同步功能都是围绕 Actor 来实现的。）<br>
<br>
在正常情况下，只有一个 NetDriver（在客户端和服务器上创建）用于“标准”游戏流量和连接。<br>
<br>
服务器 NetDriver 将维护一个 NetConnections 列表，每个连接代表游戏中的一个玩家。它负责复制 Actor 数据。<br>
<br>
客户端 NetDrivers 将具有一个代表到服务器的连接的单个 NetConnection。<br>
<br>
在服务器和客户端上，NetDriver 负责接收来自网络的数据包并将这些数据包传递给适当的 NetConnection（必要时建立新的 NetConnections）。<br>
<br>
<strong>Initiating Connections / Handshaking Flow.</strong><br>
<br>
UIpNetDriver 和 UIpConnection 是几乎所有平台引擎默认的，描述了它们如何建立和管理连接。服务器和客户端都将拥有自己的网络驱动程序，所有 UE 复制的游戏流量都将被发送或接收从 IpNetDriver。还包括用于建立连接的逻辑，以及在需要时重新建立连接的逻辑。<br>
<br>
握手分为几个不同的地方：NetDriver, PendingNetGame, World, PacketHandlers，也许还有其它地方。分开来是由于有不同的需要，例如：确定传入连接是否在“UE 协议”中发送数据，确定一个地址是否是恶意的，一个给定的客户端是否有一个游戏的正确版本，等等。<br>
<br>
<strong>启动和握手</strong><br>
<br>
当服务器加载地图（通过 UEngine:<img src="https://img.gameres.com/static/image/smiley/default/sweat.gif" smilieid="10" border="0" alt referrerpolicy="no-referrer">oadMap）时，我们将调用 UWorld::Listen。该代码负责创建主游戏网络驱动程序、解析设置并调用 UNetDriver::InitListen。最终，这些代码将负责弄清楚我们究竟是如何监听客户端连接的。例如，在 IpNetDriver 中，我们将通过调用已配置的 Socket 子系统来确定要绑定到的 IP 和端口。一旦服务器正在侦听，就可以开始接受客户端连接了。<br>
<br>
每当一个客户端想要加入一个服务器时，它们首先会在 UEngine::Browse 中通过服务器的 IP 建立一个新的 UPendingNetGame。UPendingNetGame::Initialize 和 UPendingNetGame::InitNetDriver 分别负责初始化设置和设置 NetDriver，作为初始化的一部分，客户端将立即为服务器设置一个 UNetConnection，并开始在该连接上向服务器发送数据，启动握手过程。<br>
<br>
在客户端和服务器上，UNetDriver::TickDispatch 通常负责接收网络数据。当我们收到一个数据包时，我们会检查它的地址，看它是否来自我们已经知道的连接。我们只需保存一个从 FInternetAddr 到 UNetConnection 的映射，就可以确定是否已经为给定的源地址建立了连接。如果数据包来自已经建立的连接，我们将通过 UNetConnection:：ReceivedRawPacket 将数据包传递给连接。如果数据包不是来自已经建立的连接，我们将其视为“无连接”，并开始握手过程。<br>
<br>
<strong>通知控制消息</strong><br>
<br>
当 UNetDriver 和 UNetConnection 在客户端和服务器上完成握手过程后，客户端将调用 UPendingNetGame::SendInitialJoin 来启动游戏级握手。游戏级的握手是通过一组更加结构化和复杂的 FNetControlMessages 来完成的。可以在 DataChannel.h 中找到完整的控制消息集。<br>
<br>
处理这些控制消息的大部分工作是在 UWorld::NotifyControlMessage 和 UPendingNetGame::NotifyControlMessage 中完成的。简而言之，流程如下所示：<br>
<br>
<ul><li>客户端的 UPendingNetGame:：SendInitialJoin 发送 NMT_Hello</li><li>服务器的 UWorld::NotifyControlMessage 接收 NMT_Hello，发送 NMT_Challenge</li><li>客户端的 UPendingNetGame::NotifyControlMessage 接收 NMT_Challenge，发回数据 NMT_Login</li><li>服务器的 UWorld::NotifyControlMessage 接收 NMT_Login，验证数据，然后调用 AGameModeBase:<img src="https://img.gameres.com/static/image/smiley/default/tongue.gif" smilieid="7" border="0" alt referrerpolicy="no-referrer">reLogin，如果 PreLogin 没有报告任何错误，服务器将调用 UWorld::WelcomePlayer，这将调用 AGameModeBase::GameWelcomePlayer 并发送携带地图信息的 NMT_Welcome。</li><li>客户端的 UPendingNetGame::NotifyControlMessage 接收 NMT_Welcome，读取地图信息（以便稍后开始加载），并以客户端配置的网速发送 NMT_NetSpeed。</li><li>服务器的 UWorld::NotifyControlMessage 接收 NMT_NetSpeed，并适当调整连接的网速。<br>
</li></ul><br>
在这一点上，握手被认为是完整的，玩家完全连接到游戏。根据加载地图所需的时间，客户端进入 UWorld 之前仍然可以在 UPendingNetGame 上接收一些非握手控制消息。如果需要的话，还可以使用其它步骤来处理加密。<br>
<br>
<strong>重新建立丢失的连接</strong><br>
<br>
在整个游戏过程中，可能会有很多原因导致连接丢失。网络可能退出，玩家可能离开游戏，等等。如果服务器启动了其中一个断开连接，或以其它方式意识到它（由于超时或错误），然后断开连接将通过关闭 UNetConnection 并通知游戏来处理。在这一点上，由游戏来决定它们是否支持 Join In Progress 或者 Rejoins。如果游戏确实支持它，我们将完全重新启动握手流，如上所述。<br>
<br>
如果某个东西只是短暂的中断了客户机的连接，但服务器从未意识到，然后引擎或者游戏通常会自动恢复（尽管有一些包丢失或者延迟峰值）。但是，如果客户机的IP地址或端口由于任何原因发生更改，但服务器没有意识到这一点，然后我们将通过重做低级别握手来开始恢复过程。在这种情况下，游戏代码不会被提醒。<br>
<br>
<strong>数据传输</strong><br>
<br>
游戏网络连接 NetConnections 和网络驱动 NetDrivers 通常与所使用的底层通信技术方法或技术无关。这由子类决定，比如 UIpConnection、UIpNetDriver。相反，UNetDriver 和 UNetConnection 处理 Packets 和 Bunches。<br>
<br>
Packets 是在主机和客户机上的网络连接对之间发送的数据块，由关于 Packet 包的元数据（如报头信息和确认 Ack）和 Bunches 组成。<br>
<br>
Bunches 是在主机和客户机上的通道对之间发送的数据块。当一个连接接收到一个数据包时，该数据包将被分解成单独的 Bunch，这些 Bunch 然后被传递到单独的通道以进一步处理。<br>
<br>
一个 Packet 可以不包含 Bunch、单个 Bunch 或者多个 Bunch。由于 Bunch 的大小限制可能大于单个分组的大小限制，因此引擎支持部分 Bunch 的概念。当一个 Bunch 太大时，在传输之前，我们会把它切成许多小 Bunch，这些 Bunch 将被标记为 PartialInitial, Partial 或 PartialFinal。利用这些信息，我们可以在接收端重新组装 Bunch。<br>
<br>
举个例子：客户端往服务器发送 RPC<br>
<br>
<ul><li>客户端调用 RPC</li><li>该请求被转发（通过 NetDriver 和 NetConnection）到拥有调用 RPC 的 Actor 的 Actor 通道</li><li>Actor 通道将 RPC 标识符和参数序列化为一个 Bunch。该 Bunch 还将包含其 Actor 通道的 ID</li><li>然后，Actor 通道将请求 NetConnection 发送 Bunch</li><li>稍后，NetConnection 将把这些（和其他）数据组合成一个数据包 Packet，并发送到服务器</li><li>在服务器上，网络驱动程序 NetDriver 将接收数据包</li><li>网络驱动程序 NetDriver 将检查发送数据包的地址，并将数据包移交给适当的网络连接 NetConnection</li><li>网络连接 NetConnection 将数据包分解成 Bunch（一个接一个）</li><li>NetConnection 将使用 Bunch 上的通道 ID 将 Bunch 路由到对应的 Actor 通道</li><li>ActorChannel 解码 Bunch，查看它包含的 RPC 数据，并使用 RPC ID 和序列化参数</li><li>对 Actor 调用对应的函数<br>
</li></ul><br>
<strong>可靠性和重传</strong><br>
<br>
UE4 网络通常假定基础网络协议不能保证可靠性，相反，它实现了自己的可靠性和 Packet、Bunch 的重传。<br>
<br>
当一个网络连接建立后，它将为它的 Packet 和 Bunch 建立一个序列号。这些可以是固定的，也可以是随机的（随机化后，序列将由服务器发送）。<br>
<br>
数据包编号为每个网络连接的数据包编号，每发送一个数据包，每个数据包都会包含其数据包编号，而且我们永远不会重新传输具有相同数据包编号的数据包。<br>
<br>
Bunch 序列号是每个通道的，每发送一个可靠 Bunch 就递增它的 Bunch 序列号。不过，与数据包不同的是，可以重新传输可靠的 Bunch 数据。这意味着我们将重新发送具有相同 Bunch 序列号的 Bunch。<br>
<br>
有一点要注意的是，在整个代码中，上面描述的 Packet 序列号和 Bunch 序列号通常都是序列号，只不过为了更清楚的理解，我们在这里做了区分。<br>
<br>
<strong>检测接收的丢弃数据包</strong><br>
<br>
通过分配数据包编号，我们可以很容易的检测到传入的数据包何时丢失。这只需要取最后一个成功接收的数据包编号和正在处理的当前数据包的数据包编号。<br>
<br>
<ul><li>在良好的条件下，所有数据包都将按发送顺序接收，这意味着差异将是 +1。</li><li>如果差异大于 1，则表示丢失了一些数据包。我们只是假设丢失的数据包已被丢弃，但认为当前数据包已被成功接收，用它的号码往前走。</li><li>如果差值为负数或 0，则表示我们接收到的数据包有误，或者是外部错误服务正在尝试向我们重新发送数据（请记住，引擎不会重用序列号）。<br>
</li></ul><br>
在这两种情况下，引擎通常会忽略丢失或无效的数据包，并且不会为它们发送 ack。我们确实有办法修复在同一帧上接收到的无序数据包。启用时，如果我们检测到丢失的数据包（差异 > 1），我们将不会立即处理当前数据包。相反，会将其添加到队列中。下一次成功接收数据包时（差异 = 1），我们将看看我们的队列的头排的是否正确，如果是，我们会处理，否则我们会继续接收数据包。<br>
<br>
一旦我们读取了当前可用的所有数据包，我们将刷新这个队列来处理任何剩余的数据包。在这一点上，丢失的任何东西都将被认为是被丢弃的。成功接收到的每个数据包都将其数据包编号作为确认（Ack）发送回发送方。<br>
<br>
<strong>检测发送的丢弃数据包</strong><br>
<br>
如上所述，每当成功接收到包时，接收者将发回 Ack。这些Ack将按顺序包含成功的接收的数据包的数据包序列号。与接收方跟踪数据包序列号的方式类似，发送方将跟踪最高的已确认数据包序列号。当 Ack 被处理时，任何低于我们最后收到的 Ack 的 Ack 都将被忽略，并且数据包序列号中的任何间隙都将被视为未确认。发送方负责处理这些 Ack 和 Nak 并重新发送任何丢失的数据。新数据将被添加到新的传出数据包中（同样，我们不会重新发送已经发送的数据包，或者重用数据包序列号）。<br>
<br>
<strong>重新发送丢失的数据</strong><br>
<br>
如上所述，数据包本身并不包含有用的游戏数据，相反，它们是由 Bunch 组成的有意义的数据。Bunch 可以被标记为可靠的或不可靠的。<br>
<br>
如果不可靠的 Bunch 被丢弃，引擎将不会尝试重新发送它们。因此，如果被标记为不可靠，游戏或引擎应该能够在没有它们的情况下继续，或者必须建立外部重试机制，或者必须冗余发送数据。因此，以下所有内容仅适用于可靠 Bunch。<br>
<br>
但是，引擎将尝试重新发送可靠的 Bunch。无论何时发送可靠的 Bunch，它都将添加到未确认的可靠 Bunch 列表中。如果我们收到一个包的 Nak，引擎将重新传输该 Bunch 的精确副本。注意，因为 Bunch 可能是部分的，所以即使删除一个部分 Bunch 也会导致整个 Bunch 的重新传输。当一个完整的 Bunch 的所有部分 Bunch 都已确认，我们将从列表中删除它。<br>
<br>
与数据包类似，我们将比较接收到的可靠 Bunch 的 Bunch 序列号与最后成功接收到的 Bunch 序列号。如果我们发现差异是负的，我们就忽略这个 Bunch。如果差异大于 1，我们将假设我们错过了这个 Bunch，与数据包处理不同，我们不会丢弃这些数据。相反，我们将对该 Bunch 进行排队，并暂停对任何 Bunch（可靠或不可靠）的处理。在检测到已接收到丢失的 Bunch 之前，不会恢复处理，此时我们将处理它们，然后开始处理排队的 Bunch。在等待丢失的 Bunch 时收到的任何新的 Bunch，或者在队列中仍有任何 Bunch时，都将添加到队列中，而不是立即进行处理。<br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">网络框架图 </font></strong><br>
<br>
<div align="center">
<img id="aimg_979048" aid="979048" zoomfile="https://di.gameres.com/attachment/forum/202105/18/130708jkwio4bbwr4xs8i8.png" data-original="https://di.gameres.com/attachment/forum/202105/18/130708jkwio4bbwr4xs8i8.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/18/130708jkwio4bbwr4xs8i8.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">源码分析</font></strong><br>
<br>
<strong>基本概念</strong><br>
<br>
源码版本 4.25<br>
<br>
<strong>TSequenceHistory</strong><br>
<br>
这个是用来管理接收到的序列号历史记录的，当我们接收包的时候，一般会产生一个 Ack 或者 Nak，Ack 是 1，Nak 是 0，按顺序写入 Storage 中，Storage 是一个 uint32 数组，最多存储 256 位，当超过 MaxSequenceHistoryLength 的时候，会执行 FlushNet 立即发送。 结构清晰了，那么判断某个序列号是 Ack 或者 Nak 的时候，只需要根据索引查找具体的位判断是否为 1 即可。写入的时候根据序列号的数量写入对应数量的 WordT 即可。<br>
<br>
<div class="blockcode"><div id="code_Ki6"><ol><li><p>enum &#123; MaxSequenceHistoryLength = 256 &#125;;</p><p>HistorySize = MaxSequenceHistoryLength</p><p><br>
</li><li></p><p>static constexpr SIZE_T BitsPerWord = sizeof(WordT) * 8;// = 32</p><p>static constexpr SIZE_T WordCount = HistorySize / BitsPerWord;// = 8</p><p>WordT Storage[WordCount];</p><p><br>
</li><li></p><p>template <SIZE_T HistorySize></p><p>void TSequenceHistory<HistorySize>::AddDeliveryStatus(bool Delivered)</p><p>&#123;</p><p><span style="white-space:pre">        </span>WordT Carry = Delivered ? 1u : 0u;</p><p><span style="white-space:pre">        </span>const WordT ValueMask = 1u << (BitsPerWord - 1);</p><p><span style="white-space:pre">        </span></p><p><span style="white-space:pre">        </span>for (SIZE_T CurrentWordIt = 0; CurrentWordIt < WordCount; ++CurrentWordIt)</p><p><span style="white-space:pre">        </span>&#123;</p><p><span style="white-space:pre">                </span>const WordT OldValue = Carry;</p><p><span style="white-space:pre">                </span></p><p><span style="white-space:pre">                </span>// carry over highest bit in each word to the next word</p><p><span style="white-space:pre">                </span>Carry = (Storage[CurrentWordIt] & ValueMask) >> (BitsPerWord - 1);</p><p><span style="white-space:pre">                </span>Storage[CurrentWordIt] = (Storage[CurrentWordIt] << 1u) | OldValue;</p><p><span style="white-space:pre">        </span>&#125;</p><p>&#125;</p></li></ol></div><em onclick="copycode($('code_Ki6'));">复制代码</em></div><br>
<strong>FNetPacketNotify</strong><br>
<br>
网络包通知用于实现可靠性的序列数据，包括序列号的发送，确认，以及包头数据和接收 Ack 的相关处理。<br>
<br>
<strong>FNotificationHeader</strong><br>
<br>
这是网络数据的包头结构，每个数据包会携带当前的序列号信息。OutSeq 是发送序列号，当 FlushNet 发包的时候才会自增；InAckSeq 是接收序列号，当我们收包的时候，不管是 Ack 还是 Nak，都会自增；WrittenHistoryWordCount 是记录的历史序列号的数量对 BitsPerWord 求余的结果，最小是1，最大是8。<br>
<br>
<div class="blockcode"><div id="code_k6I"><ol><li><p>struct FNotificationHeader</p><p>&#123;</p><p><span style="white-space:pre">        </span>SequenceHistoryT History;</p><p>    SIZE_T HistoryWordCount;    // = WrittenHistoryWordCount</p><p><span style="white-space:pre">        </span>SequenceNumberT Seq;        // = OutSeq</p><p><span style="white-space:pre">        </span>SequenceNumberT AckedSeq;   // = InAckSeq</p><p>&#125;;</p></li></ol></div><em onclick="copycode($('code_k6I'));">复制代码</em></div><br>
包头序列化的时候会压缩在一个 uint32 中，14 位的 Seq，14 位的 AckedSeq，4位的 HistoryWordCount。 4位是因为历史记录数组最大数量是8，14位是因为兼容历史？<br>
<br>
<div class="blockcode"><div id="code_cvI"><ol><li><p>static_assert(FNetPacketNotify::SequenceNumberBits <= 14, "SequenceNumbers must be smaller than 14 bits to fit history word count");</p><p><br>
</li><li></p><p>static uint32 Pack(SequenceNumberT Seq, SequenceNumberT AckedSeq, SIZE_T HistoryWordCount)</p><p>&#123;</p><p><span style="white-space:pre">        </span>uint32 Packed = 0u;</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>Packed |= Seq.Get() << SeqShift;</p><p><span style="white-space:pre">        </span>Packed |= AckedSeq.Get() << AckSeqShift;</p><p><span style="white-space:pre">        </span>Packed |= HistoryWordCount & HistoryWordCountMask;</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>return Packed;</p><p>&#125;</p></li></ol></div><em onclick="copycode($('code_cvI'));">复制代码</em></div><br>
那么问题来了？14位的序列号的回绕是怎么解决的呢？<br>
<br>
序列号的类型是一个 SequenceNumberT，通过 TSequenceNumber 封装。构造函数只取 SequenceNumberBits 位的数字；当自增的时候调用 Increment 去构造一个新的 TSequenceNumber，自动从头开始；比较大小的前提是，回绕后的增量小于2^(n-1)；做差值的时候取对应 SequenceNumberBits 位的数字（前提是(A - B) < SeqNumberHalf，也就是 A >= B）。<br>
<br>
<div class="blockcode"><div id="code_zdd"><ol><li><p>typedef TSequenceNumber<SequenceNumberBits, uint16> SequenceNumberT;</p><p><br>
</li><li></p><p>TSequenceNumber(SequenceT ValueIn) : Value(ValueIn & SeqNumberMask) &#123;&#125;</p><p>void Increment(SequenceT InValue) &#123; *this = TSequenceNumber(Value + InValue); &#125;</p><p><br>
</li><li></p><p>/** return true if this is > Other, this is only considered to be the case if (A - B) < SeqNumberHalf since we have to be able to detect wraparounds */</p><p>bool operator>(const TSequenceNumber& Other) const &#123; return (Value != Other.Value) && (((Value - Other.Value) & SeqNumberMask) < SeqNumberHalf); &#125;</p><p><br>
</li><li></p><p>template <SIZE_T NumBits, typename SequenceType></p><p>typename TSequenceNumber<NumBits, SequenceType>::DifferenceT TSequenceNumber<NumBits, SequenceType>::Diff(TSequenceNumber A, TSequenceNumber B) </p><p>&#123; </p><p><span style="white-space:pre">        </span>constexpr SIZE_T ShiftValue = sizeof(DifferenceT)*8 - NumBits;</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>const SequenceT ValueA = A.Value;</p><p><span style="white-space:pre">        </span>const SequenceT ValueB = B.Value;</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>return (DifferenceT)((ValueA - ValueB) << ShiftValue) >> ShiftValue;</p><p>&#125;;</p></li></ol></div><em onclick="copycode($('code_zdd'));">复制代码</em></div><br>
<strong><font color="#de5650">消息的发送</font></strong><br>
<br>
我们的消息发送都是通过 UChannel 来处理的，通过调用 UChannel::SendBunch 统一处理。 发送的 Bunch 是以 FOutBunch 的形式存在的。当 bReliable 为 True 的时候，表示 Bunch 是可靠的。<br>
<br>
<strong>1、判断上限</strong><br>
<br>
SendBunch 的时候会去判断当前 Bunch 的大小是否超出限制。IsBunchTooLarge 会判断是否超出 64K。<br>
<br>
<div class="blockcode"><div id="code_eIV"><ol><li><p>if (IsBunchTooLarge(Connection, Bunch))</p><p>&#123;</p><p><span style="white-space:pre">        </span>Bunch->SetError();</p><p><span style="white-space:pre">        </span>return FPacketIdRange(INDEX_NONE);</p><p>&#125;</p></li></ol></div><em onclick="copycode($('code_eIV'));">复制代码</em></div><br>
<strong>2、考虑合并</strong><br>
<br>
有些情况下是可以进行数据合并的，同一个 Channel 通道，可靠性一样，合并后没有超过单个 Bunch 的限制，可以合并为一个 Bunch。当然，如果是 Actor 初始化的时候需要同步 NetGUID 相关信息，这些是肯定不能合并的。<br>
<br>
<strong>3、考虑拆分</strong><br>
<br>
如果当前 Bunch 的大小超过限制时，会进行拆分，分成许多小的 Bunch。拆分 Bunch 的 bPartial 字段为1，表示分组，bPartialInitial = 1 为拆分的第一个 Bunch，表示开始，bPartialFinal = 1 为最后一个，表示结束，bOpen 和 bClose 也分别与第一个和最后一个 Bunch 有关。这些信息可以在接收的时候重新组成完整的 Bunch。<br>
<br>
<div class="blockcode"><div id="code_jvI"><ol><li><p>// MAX_SINGLE_BUNCH_SIZE_BITS = 7625</p><p>// MAX_PARTIAL_BUNCH_SIZE_BITS = 7624</p><p><br>
</li><li></p><p>if( Bunch->GetNumBits() > MAX_SINGLE_BUNCH_SIZE_BITS )</p><p>&#123;</p><p><span style="white-space:pre">        </span>uint8 *data = Bunch->GetData();</p><p><span style="white-space:pre">        </span>int64 bitsLeft = Bunch->GetNumBits();</p><p><span style="white-space:pre">        </span>Merge = false;</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>while(bitsLeft > 0)</p><p><span style="white-space:pre">        </span>&#123;</p><p><span style="white-space:pre">                </span>FOutBunch * PartialBunch = new FOutBunch(this, false);</p><p><span style="white-space:pre">                </span>int64 bitsThisBunch = FMath::Min<int64>(bitsLeft, MAX_PARTIAL_BUNCH_SIZE_BITS);</p><p><span style="white-space:pre">                </span>PartialBunch->SerializeBits(data, bitsThisBunch);</p><p><br>
</li><li></p><p><span style="white-space:pre">                </span>OutgoingBunches.Add(PartialBunch);</p><p><span style="white-space:pre">        </span></p><p><span style="white-space:pre">                </span>bitsLeft -= bitsThisBunch;</p><p><span style="white-space:pre">                </span>data += (bitsThisBunch >> 3);</p><p><span style="white-space:pre">        </span>&#125;</p><p>&#125;</p><p>else</p><p>&#123;</p><p><span style="white-space:pre">        </span>OutgoingBunches.Add(Bunch);</p><p>&#125;</p></li></ol></div><em onclick="copycode($('code_jvI'));">复制代码</em></div><br>
<strong>4、判断溢出</strong><br>
<br>
如果设置了拆分的可靠 Bunch 上限 GCVarNetPartialBunchReliableThreshold，当拆分后的列表 OutgoingBunches 的数量超过阈值的时候，并且可靠列表没有超出缓冲大小的时候，会标记为可靠的，同时会暂停复制，直到收到了所有可靠消息的 Ack；<br>
<br>
当可靠列表溢出的时候，连接会关闭。NumOutRec 为当前可靠的 Bunch 的数量，所以可靠 Bunch 的数量最多256个。<br>
<br>
<div class="blockcode"><div id="code_jvs"><ol><li><p>// RELIABLE_BUFFER = 256</p><p><br>
</li><li></p><p>const bool bOverflowsReliable = (NumOutRec + OutgoingBunches.Num() >= RELIABLE_BUFFER + Bunch->bClose);</p><p><br>
</li><li></p><p>if ((GCVarNetPartialBunchReliableThreshold > 0) && (OutgoingBunches.Num() >= GCVarNetPartialBunchReliableThreshold) && !Connection->IsInternalAck())</p><p>&#123;</p><p><span style="white-space:pre">        </span>if (!bOverflowsReliable)</p><p><span style="white-space:pre">        </span>&#123;</p><p><span style="white-space:pre">                </span>Bunch->bReliable = true;</p><p><span style="white-space:pre">                </span>bPausedUntilReliableACK = true;</p><p><span style="white-space:pre">        </span>&#125;</p><p>&#125;</p><p><br>
</li><li></p><p>if (Bunch->bReliable && bOverflowsReliable)</p><p>&#123;</p><p><span style="white-space:pre">        </span>FString ErrorMsg = NSLOCTEXT("NetworkErrors", "ClientReliableBufferOverflow", "Outgoing reliable buffer overflow").ToString();</p><p><span style="white-space:pre">        </span>FNetControlMessage<NMT_Failure>::Send(Connection, ErrorMsg);</p><p><span style="white-space:pre">        </span>Connection->FlushNet(true);</p><p><span style="white-space:pre">        </span>Connection->Close();</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>return PacketIdRange;</p><p>&#125;</p></li></ol></div><em onclick="copycode($('code_jvs'));">复制代码</em></div><br>
<strong>5、可靠 Bunch 预处理</strong><br>
<br>
调用 SendRawBunch 之前会有预处理，执行PrepBunch，当可靠的时候，<br>
<br>
<ul><li>OutReliable 保存着每个 Channel 的可靠 Bunch 数量，会去初始化 Bunch 的通道序列号 ChSequence，可以看出每个通道的可靠 Bunch 序列号是递增的。</li><li>调整可靠数据包的数量 NumOutRec</li><li>加入到 OutRec（发送的未确认的可靠消息数据）中，用于重传。只保存可靠的 Bunch。<br>
</li></ul><br>
<div class="blockcode"><div id="code_AtO"><ol><li><p>Bunch->Next<span style="white-space:pre">        </span>= NULL;</p><p>Bunch->ChSequence = ++Connection->OutReliable[ChIndex];</p><p>NumOutRec++;</p><p>OutBunch = new FOutBunch(*Bunch);</p><p>FOutBunch** OutLink = &OutRec;</p><p>while(*OutLink) // This was rewritten from a single-line for loop due to compiler complaining about empty body for loops (-Wempty-body)</p><p>&#123;</p><p><span style="white-space:pre">        </span>OutLink=&(*OutLink)->Next;</p><p>&#125;</p><p>*OutLink = OutBunch;</p></li></ol></div><em onclick="copycode($('code_AtO'));">复制代码</em></div><br>
<strong>6、SendRawBunch</strong><br>
<br>
UChannel::SendRawBunch<br>
<br>
会重置 Ack 确认标记 ReceivedAck 为0，并根据 bClose 标记设置 Channel 的状态，把当前 Channel 的 OutBunch 传给 UNetConnection。<br>
<br>
<strong>7、SendRawBunch</strong><br>
<br>
UNetConnection::SendRawBunch<br>
<br>
设置敏感标记 TimeSensitive 为1，把当前的 OutBunch 写入发送缓冲区 SendBuffer 中，缓冲区满了会调用 FlushNet 立即发送出去。当前，写入缓冲区之前会调用函数 PrepareWriteBitsToSendBuffer 预处理，判断当前的 Bunch 写入缓冲区之后是否会溢出，如果会溢出，则调用 FlushNet 立即发送出去，并且重置缓冲区 SendBuffer。<br>
<br>
<strong>8、发送时机</strong><br>
<br>
那么什么时候去 Flush 呢？正常情况下是在 UNetConnection::Tick 的时候，会判断是否有敏感标记或者超时的时候。<br>
<br>
TimeSensitive：敏感标记，是否立即发送。比如调用 SendRawBunch 的时候或者收到数据包有 DirtyAcks 的时候<br>
<br>
<div class="blockcode"><div id="code_XIe"><ol><li><p>// KeepAliveTime = 0.2</p><p>// Flush.</p><p>if ( TimeSensitive || (Driver->GetElapsedTime() - LastSendTime) > Driver->KeepAliveTime)</p><p>&#123;</p><p><span style="white-space:pre">        </span>bool bHandlerHandshakeComplete = !Handler.IsValid() || Handler->IsFullyInitialized();</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>// Delay any packet sends on the server, until we've verified that a packet has been received from the client.</p><p><span style="white-space:pre">        </span>if (bHandlerHandshakeComplete && HasReceivedClientPacket())</p><p><span style="white-space:pre">        </span>&#123;</p><p><span style="white-space:pre">                </span>FlushNet();</p><p><span style="white-space:pre">        </span>&#125;</p><p>&#125;</p></li></ol></div><em onclick="copycode($('code_XIe'));">复制代码</em></div><br>
<strong>9、发送</strong><br>
<br>
当调用 FlushNet 的时候，会重置 TimeSensitive ，并且判断发送缓冲区是否有数据，或者是否 ack 包，或者是否心跳包，才会去真正发送。<br>
<br>
<div class="blockcode"><div id="code_yB6"><ol><li><p>TimeSensitive = 0;</p><p><br>
</li><li></p><p>// If there is any pending data to send, send it.</p><p>if (SendBuffer.GetNumBits() || HasDirtyAcks || ( Driver->GetElapsedTime() - LastSendTime > Driver->KeepAliveTime && !IsInternalAck() && State != USOCK_Closed))</p></li></ol></div><em onclick="copycode($('code_yB6'));">复制代码</em></div><br>
实际的最底层发送是 FSocketBSD::SendTo 。<br>
<br>
<div class="blockcode"><div id="code_LVb"><ol><li><p>bool FSocketBSD::SendTo(const uint8* Data, int32 Count, int32& BytesSent, const FInternetAddr& Destination)</p><p>&#123;</p><p><span style="white-space:pre">        </span>// TODO: Consider converting IPv4 addresses to v6 when needed</p><p><span style="white-space:pre">        </span>if (Destination.GetProtocolType() != GetProtocol())</p><p><span style="white-space:pre">        </span>&#123;</p><p><span style="white-space:pre">                </span>return false;</p><p><span style="white-space:pre">        </span>&#125;</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>const FInternetAddrBSD& BSDAddr = static_cast<const FInternetAddrBSD&>(Destination);</p><p><span style="white-space:pre">        </span>// Write the data and see how much was written</p><p><span style="white-space:pre">        </span>BytesSent = sendto(Socket, (const char*)Data, Count, 0, (const sockaddr*)&(BSDAddr.Addr), BSDAddr.GetStorageSize());</p><p><br>
</li><li></p><p>//<span style="white-space:pre">        </span>NETWORK_PROFILER(FSocket::SendTo(Data,Count,BytesSent,Destination));</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>bool Result = BytesSent >= 0;</p><p><span style="white-space:pre">        </span>if (Result)</p><p><span style="white-space:pre">        </span>&#123;</p><p><span style="white-space:pre">                </span>LastActivityTime = FPlatformTime::Seconds();</p><p><span style="white-space:pre">        </span>&#125;</p><p><span style="white-space:pre">        </span>return Result;</p><p>&#125;</p></li></ol></div><em onclick="copycode($('code_LVb'));">复制代码</em></div><br>
发送后会调用 InitSendBuffer 重置发送缓冲区。<br>
<br>
<strong><font color="#de5650">发送堆栈 </font></strong><br>
<br>
<div align="center">
<img id="aimg_979049" aid="979049" zoomfile="https://di.gameres.com/attachment/forum/202105/18/130709m6ens6n6nodnh6nq.png" data-original="https://di.gameres.com/attachment/forum/202105/18/130709m6ens6n6nodnh6nq.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/18/130709m6ens6n6nodnh6nq.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">消息的接收</font></strong><br>
<br>
<strong>1、TickDispatch</strong><br>
<br>
UIpNetDriver::TickDispatch<br>
<br>
TickDispatch 负责接收网络数据，然后分发到对应的 NetConnection 中。所有的接收包都是通过数据包迭代器 FPacketIterator 来实现的，每次迭代调用 AdvanceCurrentPacket 来取数据包，最底层也是调用 FSocketBSD::RecvFrom 去接收的。每次接收到一个数据包，都会通过它的地址找到对应的连接 NetConnection，没有则创建新的连接并开始初始化连接的流程，传递给对应的连接调用函数 ReceivedRawPacket 处理。DDoS 侦查也是在这一阶段，比如空的数据包。<br>
<br>
<strong>2、ReceivedRawPacket</strong><br>
<br>
UNetConnection::ReceivedRawPacket<br>
<br>
每个进来或者出去的数据包都会在 PacketHandler 中做处理，比如握手，校验，加密，压缩等。<br>
<br>
<strong>3、ReceivedPacket</strong><br>
<br>
UNetConnection::ReceivedPacket<br>
<br>
这一步进行了丢包检测。读取数据包头信息，并根据包头携带的序列号信息和最后一个成功接收到的序列号去判断序列号的增量，正常情况下，所有数据包都会按发出的顺序接收，所有增量会相差1。如果大于1，说明发生了丢包，不会立即处理当前的数据，会把当前的数据包加入队列 PacketOrderCache 中。如果小于1，说明接收到的数据包发生了失序，引擎发送的每一个数据包序列号都是唯一的，不会重用，这种情况下引擎会忽略无效的数据包。<br>
<br>
<div class="blockcode"><div id="code_p6i"><ol><li><p>const int32 PacketSequenceDelta = PacketNotify.GetSequenceDelta(Header);</p><p>if (PacketSequenceDelta > 0)</p><p>&#123;</p><p><span style="white-space:pre">        </span>const bool bPacketOrderCacheActive = !bFlushingPacketOrderCache && PacketOrderCache.IsSet();</p><p><span style="white-space:pre">        </span>const bool bCheckForMissingSequence = bPacketOrderCacheActive && PacketOrderCacheCount == 0;</p><p><span style="white-space:pre">        </span>const bool bFillingPacketOrderCache = bPacketOrderCacheActive && PacketOrderCacheCount > 0;</p><p><span style="white-space:pre">        </span>const int32 MaxMissingPackets = (bCheckForMissingSequence ? CVarNetPacketOrderMaxMissingPackets.GetValueOnAnyThread() : 0);</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>const int32 MissingPacketCount = PacketSequenceDelta - 1;</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>// Cache the packet if we are already caching, and begin caching if we just encountered a missing sequence, within range</p><p><span style="white-space:pre">        </span>if (bFillingPacketOrderCache || (bCheckForMissingSequence && MissingPacketCount > 0 && MissingPacketCount <= MaxMissingPackets))</p><p><span style="white-space:pre">        </span>&#123;</p><p><span style="white-space:pre">                </span>int32 LinearCacheIdx = PacketSequenceDelta - 1;</p><p><span style="white-space:pre">                </span>int32 CacheCapacity = PacketOrderCache->Capacity();</p><p><span style="white-space:pre">                </span>bool bLastCacheEntry = LinearCacheIdx >= (CacheCapacity - 1);</p><p><br>
</li><li></p><p><span style="white-space:pre">                </span>// The last cache entry is only set, when we've reached capacity or when we receive a sequence which is out of bounds of the cache</p><p><span style="white-space:pre">                </span>LinearCacheIdx = bLastCacheEntry ? (CacheCapacity - 1) : LinearCacheIdx;</p><p><span style="white-space:pre">                </span></p><p><span style="white-space:pre">                </span>int32 CircularCacheIdx = PacketOrderCacheStartIdx;</p><p><span style="white-space:pre">                </span>for (int32 LinearDec=LinearCacheIdx; LinearDec > 0; LinearDec--)</p><p><span style="white-space:pre">                </span>&#123;</p><p><span style="white-space:pre">                        </span>CircularCacheIdx = PacketOrderCache->GetNextIndex(CircularCacheIdx);</p><p><span style="white-space:pre">                </span>&#125;</p><p><br>
</li><li></p><p><span style="white-space:pre">                </span>TUniquePtr<FBitReader>& CurCachePacket = PacketOrderCache.GetValue()[CircularCacheIdx];</p><p><span style="white-space:pre">                </span>// Reset the reader to its initial position, and cache the packet</p><p><span style="white-space:pre">                </span>if (!CurCachePacket.IsValid())</p><p><span style="white-space:pre">                </span>&#123;</p><p><span style="white-space:pre">                        </span>CurCachePacket = MakeUnique<FBitReader>(Reader);</p><p><span style="white-space:pre">                        </span>PacketOrderCacheCount++;</p><p><br>
</li><li></p><p><span style="white-space:pre">                        </span>ResetReaderMark.Pop(*CurCachePacket);</p><p><span style="white-space:pre">                </span>&#125;</p><p><span style="white-space:pre">                </span>else</p><p><span style="white-space:pre">                </span>&#123;</p><p><span style="white-space:pre">                        </span>TotalOutOfOrderPackets++;</p><p><span style="white-space:pre">                        </span>Driver->InOutOfOrderPackets++;</p><p><span style="white-space:pre">                </span>&#125;</p><p><span style="white-space:pre">                </span>return;</p><p><span style="white-space:pre">        </span>&#125;</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>InPacketsLost += MissingPacketCount;</p><p><span style="white-space:pre">        </span>InTotalPacketsLost += MissingPacketCount;</p><p><span style="white-space:pre">        </span>Driver->InPacketsLost += MissingPacketCount;</p><p><span style="white-space:pre">        </span>Driver->InTotalPacketsLost += MissingPacketCount;</p><p><span style="white-space:pre">        </span>InPacketId += PacketSequenceDelta;</p><p>&#125;</p></li></ol></div><em onclick="copycode($('code_p6i'));">复制代码</em></div><br>
接收完数据包 ReceivedPacket 或者调用 PostTickDispatch 的时候，会再调用函数 FlushPacketOrderCache 去处理之前缓存下来的数据包。<br>
<br>
当前帧接收完所有数据包后，会调用 PostTickDispatch 执行 Dispatch 后的逻辑，如果缓存 PacketOrderCache 中有数据（可能发生了乱序，或者丢包），接受完所有数据后会直接处理。<br>
<br>
<strong>4、解析数据包头</strong><br>
<br>
每个到来的数据包都需要到 PacketNotify 中更新序列号信息。<br>
<br>
1、根据包头携带的序列号数据计算出当前确认的序列号数量，然后根据 AckRecord 去更新 InAckSeqAck<br>
<br>
2、如果超出数量上限 SequenceHistoryT::Size = 256，则视为收到 Nak<br>
<br>
3、从序列号历史记录（History Storage）中判断是 Ack 还是 Nak，然后调用对应的处理函数<br>
<br>
<div class="blockcode"><div id="code_H7G"><ol><li><p>template<class Functor></p><p>void FNetPacketNotify::ProcessReceivedAcks(const FNotificationHeader& NotificationData, Functor&& InFunc)</p><p>&#123;</p><p><span style="white-space:pre">        </span>if (NotificationData.AckedSeq > OutAckSeq)</p><p><span style="white-space:pre">        </span>&#123;</p><p><span style="white-space:pre">                </span>SequenceNumberT::DifferenceT AckCount = SequenceNumberT::Diff(NotificationData.AckedSeq, OutAckSeq);</p><p><br>
</li><li></p><p><span style="white-space:pre">                </span>// Update InAckSeqAck used to track the needed number of bits to transmit our ack history</p><p><span style="white-space:pre">                </span>InAckSeqAck = UpdateInAckSeqAck(AckCount, NotificationData.AckedSeq);</p><p><br>
</li><li></p><p><span style="white-space:pre">                </span>// ExpectedAck = OutAckSeq + 1</p><p><span style="white-space:pre">                </span>SequenceNumberT CurrentAck(OutAckSeq);</p><p><span style="white-space:pre">                </span>++CurrentAck;</p><p><br>
</li><li></p><p><span style="white-space:pre">                </span>// Everything not found in the history buffer is treated as lost</p><p><span style="white-space:pre">                </span>while (AckCount > (SequenceNumberT::DifferenceT)(SequenceHistoryT::Size))</p><p><span style="white-space:pre">                </span>&#123;</p><p><span style="white-space:pre">                        </span>--AckCount;</p><p><span style="white-space:pre">                        </span>InFunc(CurrentAck, false);</p><p><span style="white-space:pre">                        </span>++CurrentAck;</p><p><span style="white-space:pre">                </span>&#125;</p><p><br>
</li><li></p><p><span style="white-space:pre">                </span>// For sequence numbers contained in the history we lookup the delivery status from the history</p><p><span style="white-space:pre">                </span>while (AckCount > 0)</p><p><span style="white-space:pre">                </span>&#123;</p><p><span style="white-space:pre">                        </span>--AckCount;</p><p><span style="white-space:pre">                        </span>InFunc(CurrentAck, NotificationData.History.IsDelivered(AckCount));</p><p><span style="white-space:pre">                        </span>++CurrentAck;</p><p><span style="white-space:pre">                </span>&#125;</p><p><span style="white-space:pre">                </span>OutAckSeq = NotificationData.AckedSeq;</p><p><span style="white-space:pre">        </span>&#125;</p><p>&#125;</p></li></ol></div><em onclick="copycode($('code_H7G'));">复制代码</em></div><br>
<strong>5、接收 Ack</strong><br>
<br>
当接收到 Ack 的时候，会对当前确认的包 id 相同的 bunch 修改标志位 ReceivedAck，并且从 OutRec 列表中删除已确认的消息 bunch。<br>
<br>
<div class="blockcode"><div id="code_XAl"><ol><li><p>auto AckChannelFunc = [this, &OutChannelsToClose](int32 AckedPacketId, uint32 ChannelIndex)</p><p>&#123;</p><p><span style="white-space:pre">        </span>UChannel* const Channel = Channels[ChannelIndex];</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>if (Channel)</p><p><span style="white-space:pre">        </span>&#123;</p><p><span style="white-space:pre">                </span>if (Channel->OpenPacketId.Last == AckedPacketId) // Necessary for unreliable "bNetTemporary" channels.</p><p><span style="white-space:pre">                </span>&#123;</p><p><span style="white-space:pre">                        </span>Channel->OpenAcked = 1;</p><p><span style="white-space:pre">                </span>&#125;</p><p><span style="white-space:pre">                        </span></p><p><span style="white-space:pre">                </span>for (FOutBunch* OutBunch = Channel->OutRec; OutBunch; OutBunch = OutBunch->Next)</p><p><span style="white-space:pre">                </span>&#123;</p><p><span style="white-space:pre">                        </span>if (OutBunch->bOpen)</p><p><span style="white-space:pre">                        </span>&#123;</p><p><span style="white-space:pre">                                </span>UE_LOG(LogNet, VeryVerbose, TEXT("Channel %i reset Ackd because open is reliable. "), Channel->ChIndex );</p><p><span style="white-space:pre">                                </span>Channel->OpenAcked  = 0; // We have a reliable open bunch, don't let the above code set the OpenAcked state,</p><p><span style="white-space:pre">                                                                                </span>// it must be set in UChannel::ReceivedAcks to verify all open bunches were received.</p><p><span style="white-space:pre">                        </span>&#125;</p><p><br>
</li><li></p><p><span style="white-space:pre">                        </span>if (OutBunch->PacketId == AckedPacketId)</p><p><span style="white-space:pre">                        </span>&#123;</p><p><span style="white-space:pre">                                </span>OutBunch->ReceivedAck = 1;</p><p><span style="white-space:pre">                        </span>&#125;</p><p><span style="white-space:pre">                </span>&#125;</p><p><span style="white-space:pre">                </span>Channel->ReceivedAck(AckedPacketId);</p><p><span style="white-space:pre">                </span>EChannelCloseReason CloseReason;</p><p><span style="white-space:pre">                </span>if (Channel->ReceivedAcks(CloseReason))</p><p><span style="white-space:pre">                </span>&#123;</p><p><span style="white-space:pre">                        </span>const FChannelCloseInfo Info = &#123;ChannelIndex, CloseReason&#125;;</p><p><span style="white-space:pre">                        </span>OutChannelsToClose.Emplace(Info);</p><p><span style="white-space:pre">                </span>&#125;<span style="white-space:pre">        </span></p><p><span style="white-space:pre">        </span>&#125;</p><p>&#125;;</p><p><span style="white-space:pre">        </span>// Invoke AckChannelFunc on all channels written for this PacketId</p><p>FChannelRecordImpl::ConsumeChannelRecordsForPacket(ChannelRecord, AckPacketId, AckChannelFunc);</p></li></ol></div><em onclick="copycode($('code_XAl'));">复制代码</em></div><br>
<strong>6、接收 Nak</strong><br>
<br>
当我们发送一个可靠的 Bunch 的时候，会把它添加到 OutRec 中，这是一个已发送的未确认的可靠消息列表。当接收到 Nak 的时候，会为每个通道的包 id 为 NakPacketId 的未确认的可靠数据重新发送一次。丢包发生的时候，只会按 Bunch 去重新发送，Bunch 序列号还是原来的 Channel 序列号，而之前的 Packet 是不会重用的，只会生成新的 Packet，以及最新的 PacketId。意味着不会重新发送之前发送的数据包，也不会重用数据包序列号，数据包的发送每一次都是新生成的数据包，数据包序列号都是递增的，不会重复。<br>
<br>
1、由于 OutRec 只保存了可靠的数据包，如果是不可靠的消息发生了丢包，引擎是不会重新发送它们的。<br>
<br>
2、这里保存的是 RawBunch，如果 Bunch 是拆分的，丢弃了一部分，会导致整个 Bunch 的重新发送。<br>
<br>
<div class="blockcode"><div id="code_Cfx"><ol><li><p>void UChannel::ReceivedNak( int32 NakPacketId )</p><p>&#123;</p><p><span style="white-space:pre">        </span>for( FOutBunch* Out=OutRec; Out; Out=Out->Next )</p><p><span style="white-space:pre">        </span>&#123;</p><p><span style="white-space:pre">                </span>// Retransmit reliable bunches in the lost packet.</p><p><span style="white-space:pre">                </span>if( Out->PacketId==NakPacketId && !Out->ReceivedAck )</p><p><span style="white-space:pre">                </span>&#123;</p><p><span style="white-space:pre">                        </span>check(Out->bReliable);</p><p><span style="white-space:pre">                        </span>UE_LOG(LogNetTraffic, Log, TEXT("      Channel %i nak); resending %i..."), Out->ChIndex, Out->ChSequence );</p><p><span style="white-space:pre">                        </span></p><p><span style="white-space:pre">                        </span>FNetTraceCollector* Collector = Connection->GetOutTraceCollector();</p><p><span style="white-space:pre">                        </span>if (Collector)</p><p><span style="white-space:pre">                        </span>&#123;</p><p><span style="white-space:pre">                                </span>// Inject trace event for the resent bunch if tracing is enabled</p><p><span style="white-space:pre">                                </span>// The reason behind the complexity is that the outgoing sendbuffer migth be flushed during the call to SendRawBunch()</p><p><span style="white-space:pre">                                </span>FNetTraceCollector* TempCollector = UE_NET_TRACE_CREATE_COLLECTOR(ENetTraceVerbosity::Trace);</p><p><span style="white-space:pre">                                </span>UE_NET_TRACE(ResendBunch, TempCollector, 0U, Out->GetNumBits(), ENetTraceVerbosity::Trace);</p><p><span style="white-space:pre">                                </span>Connection->SendRawBunch(*Out, 0, TempCollector);</p><p><span style="white-space:pre">                                </span>UE_NET_TRACE_DESTROY_COLLECTOR(TempCollector);</p><p><span style="white-space:pre">                        </span>&#125;</p><p><span style="white-space:pre">                        </span>else</p><p><span style="white-space:pre">                        </span>&#123;</p><p><span style="white-space:pre">                                </span>Connection->SendRawBunch( *Out, 0 );</p><p><span style="white-space:pre">                        </span>&#125;</p><p><span style="white-space:pre">                </span>&#125;</p><p><span style="white-space:pre">        </span>&#125;</p><p>&#125;</p></li></ol></div><em onclick="copycode($('code_Cfx'));">复制代码</em></div><br>
<strong>7、分发bunches</strong><br>
<br>
解析数据，分发所有的Bunch。通过通道索引 ChIndex 找到对应的通道 Channel，调用函数 UChannel::ReceivedRawBunch 解析。<br>
<br>
<strong>8、ReceivedRawBunch</strong><br>
<br>
UChannel::ReceivedRawBunch<br>
<br>
1、如果是可靠的消息，但是通道序列号不是有序的，则放入接收可靠消息列表 InRec 中，并按通道序列号 ChSequence 顺序存储，同样的，接收的可靠消息列表数量 NumInRec 一样不能超过可靠缓冲区大小256（RELIABLE_BUFFER）。<br>
<br>
2、调用 ReceivedNextBunch 接收完之后，会再处理之前缓存的可靠消息列表 InRec，按顺序处理。<br>
<br>
<strong>9、ReceivedNextBunch</strong><br>
<br>
UChannel::ReceivedNextBunch<br>
<br>
1、如果是可靠消息，重置序列号<br>
<br>
2、如果是 PartialBunch，当第一个初始化 bPartialInitial 的时候，会创建 InPartialBunch，后续遇到所有的 PartialBunch 都会合并到 InPartialBunch 中。对合并后的 InPartialBunch 进行大小检查 IsBunchTooLarge，超过 64K 不处理。<br>
<br>
<strong>10、ReceivedSequencedBunch</strong><br>
<br>
UChannel::ReceivedSequencedBunch<br>
<br>
在确认有序 Bunch 后执行对应 Channel 的 ReceivedBunch 函数，处理各自 Channel 的接收逻辑，如果标记了 bClose 的 Bunch，则关闭 Channel。<br>
<br>
<strong>11、确认</strong><br>
<br>
当收到一份数据的时候，我们会对数据进行确认，会回复 Ack 或者 Nak，写入到序列号历史记录中，由于历史记录最多 256 位，所以当 Ack 累计超过之后，会调用 FlushNet 立即发送。同时改变敏感标志位 TimeSensitive。<br>
<br>
<div class="blockcode"><div id="code_J9F"><ol><li><p>if( !IsInternalAck() )</p><p>&#123;</p><p><span style="white-space:pre">        </span>// We always call AckSequence even if we are explicitly rejecting the packet as this updates the expected InSeq used to drive future acks.</p><p><span style="white-space:pre">        </span>if ( bSkipAck )</p><p><span style="white-space:pre">        </span>&#123;</p><p><span style="white-space:pre">                </span>// Explicit Nak, we treat this packet as dropped but we still report it to the sending side as quickly as possible</p><p><span style="white-space:pre">                </span>PacketNotify.NakSeq( InPacketId );</p><p><span style="white-space:pre">        </span>&#125;</p><p><span style="white-space:pre">        </span>else</p><p><span style="white-space:pre">        </span>&#123;</p><p><span style="white-space:pre">                </span>PacketNotify.AckSeq( InPacketId );</p><p><br>
</li><li></p><p><span style="white-space:pre">                </span>// Keep stats happy</p><p><span style="white-space:pre">                </span>++OutTotalAcks;</p><p><span style="white-space:pre">                </span>++Driver->OutTotalAcks;</p><p><span style="white-space:pre">        </span>&#125;</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>// We do want to let the other side know about the ack, so even if there are no other outgoing data when we tick the connection we will send an ackpacket.</p><p><span style="white-space:pre">        </span>TimeSensitive = 1;</p><p><span style="white-space:pre">        </span>++HasDirtyAcks;</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>if (HasDirtyAcks >= FNetPacketNotify::MaxSequenceHistoryLength)</p><p><span style="white-space:pre">        </span>&#123;</p><p><span style="white-space:pre">                </span>FlushNet();</p><p><span style="white-space:pre">                </span>if (HasDirtyAcks) // if acks still are dirty, flush again</p><p><span style="white-space:pre">                </span>&#123;</p><p><span style="white-space:pre">                        </span>FlushNet();</p><p><span style="white-space:pre">                </span>&#125;</p><p><span style="white-space:pre">        </span>&#125;</p><p>&#125;</p></li></ol></div><em onclick="copycode($('code_J9F'));">复制代码</em></div><br>
bSkipAck 又是如何去确认是 Nak 的呢？有几种情况：<br>
<br>
1、不可靠的数据包去打开通道，并且不是暂时的。<br>
<br>
2、不可靠的 PartialBunch 破坏了未解析完的上一个可靠的 PartialBunch。<br>
<br>
3、PartialBunch 的合并出现问题，比如序列号不匹配。<br>
<br>
4、通道未完全打开。<br>
<br>
当然确认序列号时发生丢包的情况下，也是返回 Nak。<br>
<br>
<strong>12、丢包</strong><br>
<br>
发生丢包的时候，缓存 PacketOrderCache 中肯定是有数据的，接受完所有数据后会直接处理缓存中的数据包。<br>
<br>
连接记录接收的 PacketId 是实时计算的，每收到一个数据包，InPacketId 会加上计算出的增量 PacketSequenceDelta。所以发生丢包的时候，当前计算出的 InPacketId 与上次保存的序列号 InAckSeq 之间的差值大于 1，会把中间所有丢失的序列号标记为未确认，序列号历史记录中记为 False，返回 Nak 给发送方。<br>
<i><font color="#808080"><br>
</font></i><br>
<div class="quote"><blockquote>举个例子，如果当前最后接收到的数据包序列号（InPacketId）为 3，下一帧陆续接收到了数据包序列号 8 、 6，那么接收数据包为 8 的时候会和 3 比较，差值为 5，发生了丢包，会加入到缓存 PacketOrderCache 中，在缓存中的位置为 5。同理，当接收到数据包为 6 的时候，差值为 3，在缓存中的位置是 3，这样数据包就已经排好了顺序。当所有数据包都已经接收完毕后，会按顺序处理缓存 PacketOrderCache 中的数据包 6 、8，第一次处理数据包 6 的时候，由于 InPacketId 加上当前的差值 3，所以现在已经接收到的序列号就是 6，当把 InPacketId 传入函数 AckSeq 中确认 ACK 的时候，只会确认与当前 AckedSeq 相等的序列号，中间的所有序列号都会视为丢包，这里会按顺序确认 4、5、6，4 和 5 被视为丢包，返回 NAK, 6 视为确认，返回 ACK。同理，处理数据包 8 的时候，7 被视为丢包， 8 视为确认。所以当前 ACK 历史记录中就被计为 00101，记录的是 4 - 8 的数据包确认状态，对端再根据确认状态进行 ACK 和 NAK 的处理。如果网络中的异常情况导致下一帧接收到了数据包 4，由于当前已接收到数据包序列号已经是 8，会丢弃不处理。</blockquote></div><div class="blockcode"><div id="code_Cgp"><ol><li><p>void FNetPacketNotify::AckSeq(SequenceNumberT AckedSeq, bool IsAck)</p><p>&#123;</p><p><span style="white-space:pre">        </span>check( AckedSeq == InSeq);</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>while (AckedSeq > InAckSeq)</p><p><span style="white-space:pre">        </span>&#123;</p><p><span style="white-space:pre">                </span>++InAckSeq;</p><p><br>
</li><li></p><p><span style="white-space:pre">                </span>const bool bReportAcked = InAckSeq == AckedSeq ? IsAck : false;</p><p><br>
</li><li></p><p><span style="white-space:pre">                </span>UE_LOG_PACKET_NOTIFY(TEXT("FNetPacketNotify::AckSeq - AckedSeq: %u, IsAck %u"), InAckSeq.Get(), bReportAcked ? 1u : 0u);</p><p><br>
</li><li></p><p><span style="white-space:pre">                </span>InSeqHistory.AddDeliveryStatus(bReportAcked);<span style="white-space:pre">                </span></p><p><span style="white-space:pre">        </span>&#125;</p><p>&#125;</p></li></ol></div><em onclick="copycode($('code_Cgp'));">复制代码</em></div><br>
<strong><font color="#de5650">接收堆栈 </font></strong><br>
<br>
<div align="center">
<img id="aimg_979050" aid="979050" zoomfile="https://di.gameres.com/attachment/forum/202105/18/130710tbpf01xzht7fsfjt.png" data-original="https://di.gameres.com/attachment/forum/202105/18/130710tbpf01xzht7fsfjt.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/18/130710tbpf01xzht7fsfjt.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">流量控制</font></strong><br>
<br>
下面聊一聊 UE4 是如何进行网络带宽限制的，也就是通常所说的限流。限流的实现与两个部分有关，一个是网络速度，一个是可以发送的最大流量。<br>
<br>
<strong>CurrentNetSpeed</strong><br>
<br>
当前的网络速度是一开始就初始化的，如果是局域网就读取配置中的局域网速度 ConfiguredLanSpeed，否则读取互联网速度 ConfiguredInternetSpeed。客户端连接过程中接收到消息 NMT_Welcome，会以初始化的网速发送 NMT_NetSpeed ，服务器接收 NMT_NetSpeed，并适当调整当前连接的网速。<br>
<br>
<i><font color="#808080">通过阅读源码发现，当前网速是固定的，只在连接过程中同步客户端配置的网速，此后不再改变。</font></i><br>
<br>
引擎默认配置的网速为每秒的字节数，比如默认配置中的网络速度10000，转换成通俗一点的网速是（10000 / 1024 = ）9.76 kb/s ，局域网的会快一点。通常每个项目会根据需要修改合适的网速。需要特别说明的是，如果是重播相关的 UDemoNetDriver，初始化连接的时候会传入固定的网速1000000，相当于976 kb/s。<br>
<br>
<div class="blockcode"><div id="code_Zg7"><ol><li><p>[/Script/Engine.Player]</p><p>ConfiguredInternetSpeed=10000</p><p>ConfiguredLanSpeed=20000</p></li></ol></div><em onclick="copycode($('code_Zg7'));">复制代码</em></div><br>
<strong>QueuedBits</strong><br>
<br>
这个就是当前网络可以发送的最大流量，类似于 TCP 的滑动窗口。<br>
<br>
<strong>增加</strong><br>
<br>
有了当前的网络速度，再计算时间，就可以得到当前的流量了。DeltaTime 为当前 Tick 的时间差，DesiredTickRate 为当前的期望帧率（值得一提的是，如果编辑器在后台运行，帧率会退化为3），实际的带宽时间差 BandwidthDeltaTime 会根据期望帧率去修改时间差（如果这一帧跑了太长的时间，会修复，不会有太大的偏差）。所以计算出的流量 DeltaBits 就是这一帧可以增加的流量。引擎同时做了优化，限定了当前可发送的流量（介于1倍和2倍之间），允许一部分的延迟。<br>
<br>
<strong>减少</strong><br>
<br>
当我们调用 FlushNet 去发送数据的时候，QueuedBits 会相应的减少发送的数据量。<br>
<br>
<strong>判断</strong><br>
<br>
函数 IsNetReady 用于判断网络是否畅通，当最大流量 QueuedBits 与缓冲区的差值小于0时，说明还有流量可以发送，网络畅通，可以准备写入缓冲区，如果差值大于0时，说明没有可发送的流量，缓冲区已满，网络饱和，不能继续写入。<br>
<br>
<div class="blockcode"><div id="code_aP7"><ol><li><p>int32 UNetConnection::IsNetReady( bool Saturate )</p><p>&#123;</p><p><span style="white-space:pre">        </span>if (Saturate)</p><p><span style="white-space:pre">        </span>&#123;</p><p><span style="white-space:pre">                </span>QueuedBits = -SendBuffer.GetNumBits();</p><p><span style="white-space:pre">        </span>&#125;</p><p><br>
</li><li></p><p><span style="white-space:pre">        </span>return QueuedBits + SendBuffer.GetNumBits() <= 0;</p><p>&#125;</p></li></ol></div><em onclick="copycode($('code_aP7'));">复制代码</em></div><br>
当我们上层需要进行 Actor 网络复制或者 RPC 调用时，需要判断当前网络是否饱和，如果是，则不会继续。特别的，如果是重要的 RPC 函数，比如标记了 FUNC_NetReliable 或者 FUNC_NetMulticast，尽管网络饱和，也会发送。<br>
<br>
网络连接的函数 Tick 中限流核心代码<br>
<br>
<div class="blockcode"><div id="code_E9f"><ol><li><p>float BandwidthDeltaTime = DeltaTime;</p><p>if (DesiredTickRate != 0.0f)</p><p>&#123;</p><p><span style="white-space:pre">        </span>BandwidthDeltaTime = FMath::Clamp(BandwidthDeltaTime, 0.0f, 1.0f / DesiredTickRate);</p><p>&#125;</p><p><br>
</li><li></p><p>float DeltaBits = CurrentNetSpeed * BandwidthDeltaTime * 8.f;</p><p>QueuedBits -= FMath::TruncToInt(DeltaBits);</p><p>float AllowedLag = 2.f * DeltaBits;</p><p>if (QueuedBits < -AllowedLag)</p><p>&#123;</p><p><span style="white-space:pre">        </span>QueuedBits = FMath::TruncToInt(-AllowedLag);</p><p>&#125;</p></li></ol></div><em onclick="copycode($('code_E9f'));">复制代码</em></div><br>
<strong><font color="#de5650">总结</font></strong><br>
<br>
<strong><font color="#de5650">可靠有序</font></strong><br>
<br>
1、每一个 Bunch 都是携带数据的，Bunch 大小有限制，过大会进行拆分。同一个 Channel 的多个 Bunch 有可能合并。<br>
<br>
2、Packet 里包括 Ack 和多个 Bunch，也可能没有 Bunch，只发送 Ack。<br>
<br>
3、每个 Channel 的发送接收缓冲区只会保存可靠的 Bunch，不可靠的 Bunch 没有备份，上层自己维护。上限256个。<br>
<br>
4、每一个发出去的包都有一个 Packet 序列号，如果发生丢包，只会重新发送当前 Packet 里可靠的原始未拆分的 Bunch，保证单个 Channel 内的可靠 Bunch 是有序的，Channel 间的 Bunch 有序性是不确定的，部分丢失的 Bunch 会发送完整的 Bunch，并且发送 Bunch 会重新组装成一个新的 Packet，以及新的 Packet 序列号，和丢失的 Packet 毫无关系，内部的 Bunchs 也不一定完全相同。所以可靠不是相对于 Packet 来说的，只有可靠的 Bunch。<br>
<br>
5、发生 Packet 乱序或者 Bunch 乱序的时候，会先缓存起来，等第一个有序到来的时候，再一起按序处理。<br>
<br>
6、调用 FlushNet 立即发送的时机？<br>
<br>
<ul><li>正常情况下，UNetConnection::Tick 的时候，如果设置了敏感标记 TimeSensitive，或者距离上次发送时间超过了心跳时间 KeepAliveTime 的时候</li><li>缓冲区满了</li><li>如果新加入的 Bunch 大小会使缓冲区大小越界，会立即发送已在缓冲区的数据</li><li>Ack 数量累计超过 256</li><li>需要立即关机某个 Channel</li><li>连接 NetConnection 设置了自动发送 bAutoFlush</li><li>连接关闭之前，会刷新缓冲区<br>
</li></ul><br>
7、没有超时重传，只有收到 Nak 才会重传。<br>
<br>
<strong><font color="#de5650">最后</font></strong><br>
<br>
这篇文章只是想了解 UDP 是如何进行可靠传输的，涉及到了很多的源码，更多的是我对源码的理解。如果发现有错误或者想交流学习，可以联系我。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：程序员毛寸</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/wOaC0Zf2LIeKYJ1yt00Kow</font></font><br>
<br>
<br>
</td></tr></tbody></table>



  
</div>
            