
---
title: '使用开源工具实现Kubernetes备份容灾'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211218/6d0b23349b467ea22b61f09b602ea20e.png'
author: Dockone
comments: false
date: 2021-12-25 09:07:45
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211218/6d0b23349b467ea22b61f09b602ea20e.png'
---

<div>   
<br><h3>前言</h3>Kubernetes的备份目前官方社区没有现成的成熟方案，当前使用最多的方式还是通过etcd快照做数据备份。<br>
<br>但是etcd的备份只能备份Kubernetes的资源，不能备份存储在PV数据卷的业务数据，而这些数据往往才是最核心的，Kubernetes资源没了至少可以重新Apply，业务数据丢了是毁灭性的灾难。<br>
<br>数据卷的备份可能需要取决于使用不同的PV存储后端采用不用的备份方案，以Ceph RBD为例，可以定时对RBD Image做快照，并通过快照把数据备份到对象存储系统中，或者通过Ceph mirror实现异地复制容灾。而公有云场景则可以直接使用公有云的备份服务实现对volume备份，至少AWS提供了类似这种方案。<br>
<br>如上方案是基于数据块的形式对整卷做备份，当然也可以基于文件备份，这种方式其实备份效率会更高些，用多少备多少，结合去重技术和压缩算法，可以大大节省存储空间。<br>
<br>大家可能比较容易想到的方案是通过SideCar方式注入rsync或其他备份工具实时同步文件到远端存储中实现业务数据的实时增量备份。<br>
<br>在这里我推荐<a href="https://restic.readthedocs.io/en/latest/010_introduction.html">restic</a>这款开源工具代替rsync做基于文件的备份，不仅仅适用于企业级Kubernetes环境的数据卷备份，个人的笔记本电脑备份也可以通过restic这款开源的工具实现。<br>
<br>当然现在很多现成的工具如iCloud、百度网盘等也能实现本地电脑备份同步，不过自己使用restic加密工具备份更自主可控、更安心些，价格也会更便宜。<br>
<br>总之，通过restic以SideCar的形式注入到包含PV的Pod中实现备份，技术上肯定是可行的，不过实现落地上可能会稍微复杂些，而开源的velero已经完全解决了这个问题。<br>
<br>因此本文接下来主要介绍如何利用开源的velero方案实现Kubernetes的应用备份。这里需要强调的是，虽然使用velero做了应用级别的备份，但并不意味着不再需要对Kubernetes做集群备份，etcd以及Kubernetes的证书、kubeadm的配置等依然需要在备份策略中考虑到，在集群恢复中不可或缺。<br>
<br>由于Velero备份PV数据卷正是使用了前面的restic，因此本文先简单介绍下restic的使用方法，这部分内容与Kubernetes备份没有直接关系，但是了解底层对后续使用velero恢复数据很有用，已经对restic有了解的可以跳过。<br>
<h3>restic简介</h3>restic是一款开源的跨Linux、MacOS、Windows等多种平台操作系统的命令行备份工具，支持将本地文件全量或者增量加密备份到S3、SFTP服务器、远端目录、MinIO对象存储等远端仓库中，可以代替我们常用的rsync工具。<br>
<br>restic包含如下五个设计理念：<br>
<ul><li>简单（Easy），备份和恢复只需要简单一个命令即可完成，不需要太复杂的配置和指令。</li><li>快（Fast），备份和恢复速度仅受限于网络带宽和磁盘读写速率，工具本身不应该成为性能瓶颈。</li><li>可校验（Verifiable），用户可以随时查看和检索任意备份点中备份的所有文件内容，从而确定备份是OK的。</li><li>安全（Secure），数据备份强加密存储，即使远端存储仓库泄露被攻击者拿到，攻击者也拿不到真实明文数据。</li><li>高效（Efficient），基于文件备份，只备份增量文件，自动去重，从而节省存储空间。</li></ul><br>
<br><h4>restic配置以及仓库初始化</h4>restic可以从官网直接<a href="https://github.com/restic/restic/releases/tag/v0.12.1">下载</a>，下载后建议配置自动补全：<br>
<pre class="prettyprint">restic generate --bash-completion restic.bash_completion  <br>
source restic.bash_completion<br>
</pre><br>
restic用法正如其设计原则，非常简单。首先初始化备份仓库，这里我们使用开源的Minio对象存储作为备份仓库，桶策略已提前配置好，Key和Secret通过环境变量进行配置：<br>
<pre class="prettyprint">export AWS_ACCESS_KEY_ID=93E0...2MV4K  <br>
export AWS_SECRET_ACCESS_KEY=wulg1N...rXgGR<br>
</pre><br>
使用<code class="prettyprint">init</code>子命令初始化仓库，restic为了安全性考虑，仓库时需要指定密码，密码请务必记住，密码丢了数据将无法恢复，这样做是为了防止备份仓库的数据泄露导致业务数据泄露。<br>
<pre class="prettyprint"># restic -r s3:http://int32bit-minio-server/local-backup init  <br>
enter password for new repository:  <br>
enter password again:  <br>
<br>
created restic repository 94c40f5300 at s3:http://int32bit-minio-server/local-backup<br>
</pre><br>
使用<code class="prettyprint">stats</code>子命令查看仓库状态：<br>
<pre class="prettyprint"># restic -r s3:http://int32bit-minio-server/local-backup stats  <br>
enter password for new repository:  <br>
enter password again:  <br>
repository 94c40f53 opened successfully, password is correct  <br>
scanning...  <br>
Stats in restore-size mode:  <br>
Snapshots processed:   0  <br>
     Total Size:   0 B<br>
</pre><br>
当前为空仓库，因此大小和快照数量均为0。<br>
<br>为了安全性考虑，每次对备份仓库进行查看、备份、恢复等所有操作均需要输入密码，这在生产环境上是必须的，这里为了测试方便写入环境变量中并指定仓库地址：<br>
<pre class="prettyprint">export RESTIC_PASSWORD=*********  <br>
export RESTIC_REPOSITORY=s3:http://int32bit-minio-server/local-backup<br>
</pre><br>
此时只需要直接运行<code class="prettyprint">restic stats</code>即可查看仓库信息，无需指定仓库地址以及输入密码。<br>
<pre class="prettyprint"># restic stats  <br>
scanning...  <br>
Stats in restore-size mode:  <br>
Snapshots processed:   0  <br>
     Total Size:   0 B<br>
</pre><br>
<h4>执行备份</h4>通过<code class="prettyprint">backup</code>子命令执行备份操作：<br>
<pre class="prettyprint"># mkdir -p backup-demo  <br>
# echo "hello" >backup-demo/hello.txt  <br>
# restic backup backup-demo/  <br>
no parent snapshot found, will read all files  <br>
<br>
Files:           1 new,     0 changed,     0 unmodified  <br>
Dirs:            1 new,     0 changed,     0 unmodified  <br>
Added to the repo: 754 B  <br>
<br>
processed 1 files, 6 B in 0:00  <br>
snapshot 55572d0c saved<br>
</pre><br>
首次备份因为没有父备份点，因此为全量备份，从备份中输出中我们可以查看备份的文件数量以及大小。<br>
<br>我们写入一个新文件并修改其中一个文件，再次执行备份操作：<br>
<pre class="prettyprint"># echo "new_file" >backup-demo/new_file.txt  <br>
# echo "helloworld!" >backup-demo/hello.txt  <br>
# restic backup backup-demo/  <br>
using parent snapshot 55572d0c  <br>
<br>
Files:           1 new,     1 changed,     0 unmodified  <br>
Dirs:            0 new,     1 changed,     0 unmodified  <br>
Added to the repo: 1.107 KiB  <br>
<br>
processed 2 files, 21 B in 0:00  <br>
snapshot f7d5b7c5 saved<br>
</pre><br>
可见当我们写入一个新文件并且修改了原<code class="prettyprint">hello.txt</code>文件，再次运行备份程序，此时默认为增量备份，从备份结果中我们看到新增了1个文件、修改了一个文件。<br>
<br>备份时默认会备份指定目录的所有文件，包含隐藏文件，可以通过指定<code class="prettyprint">--exclude</code>参数排除需要备份的文件，也可以通过<code class="prettyprint">--file-from</code>指定需要备份的文件列表。<br>
<br>另外可以每次备份时指定一个或者多个标签，便于后期基于tag做快照检索。<br>
<br>每次备份时都会创建一个<code class="prettyprint">snapshot</code>快照实例，backup结果会输出<code class="prettyprint">snapshot id</code>，可以通过<code class="prettyprint">snapshots</code>参数列举该仓库下的所有snapshots实例，当然也可以指定标签过滤：<br>
<pre class="prettyprint"># restic snapshots  <br>
ID        Time                 Host               Paths  <br>
--------------------------------------------------------------------  <br>
55572d0c  2021-10-11 14:09:11  int32bit-test-1    /root/backup-demo  <br>
f7d5b7c5  2021-10-11 14:12:39  int32bit-test-1    /root/backup-demo  <br>
--------------------------------------------------------------------<br>
</pre><br>
通过<code class="prettyprint">diff</code>参数查看两个snapshots的差量：<br>
<pre class="prettyprint"># restic diff 55572d0c f7d5b7c5  <br>
comparing snapshot 55572d0c to f7d5b7c5:  <br>
<br>
M    /backup-demo/hello.txt  <br>
+    /backup-demo/new_file.txt  <br>
<br>
Files:           1 new,     0 removed,     1 changed  <br>
Dirs:            0 new,     0 removed  <br>
Others:          0 new,     0 removed  <br>
Data Blobs:      2 new,     1 removed  <br>
Tree Blobs:      2 new,     2 removed  <br>
Added:   1.107 KiB  <br>
Removed: 754 B<br>
</pre><br>
<h4>文件检索以及查看文件内容</h4>通过<code class="prettyprint">ls</code>子命令可以查看指定快照中的所有文件列表：<br>
<pre class="prettyprint"># restic ls f18cccc5  <br>
snapshot f18cccc5:  <br>
/backup-demo  <br>
/backup-demo/hello.txt  <br>
/backup-demo/hello2.txt  <br>
/backup-demo/new_file.txt  <br>
# restic ls -l f18cccc5  <br>
snapshot f18cccc5:  <br>
drwxr-xr-x     0     0      0 2021-10-11 14:40:30 /backup-demo  <br>
--w-r--r--     0     0     12 2021-10-11 14:12:20 /backup-demo/hello.txt  <br>
-rw-r--r--     0     0      7 2021-10-11 14:40:30 /backup-demo/hello2.txt  <br>
-rw-r--r--     0     0      9 2021-10-11 14:11:38 /backup-demo/new_file.txt<br>
</pre><br>
通过<code class="prettyprint">find</code>命令从所有快照中查找文件，这个命令对于文件误删除后进行文件找回非常有用：<br>
<pre class="prettyprint"># restic find hello*  <br>
Found matching entries in snapshot f18cccc5 from 2021-10-11 14:40:36  <br>
/backup-demo/hello.txt  <br>
/backup-demo/hello2.txt  <br>
<br>
Found matching entries in snapshot 55572d0c from 2021-10-11 14:09:11  <br>
/backup-demo/hello.txt  <br>
<br>
Found matching entries in snapshot 7728a603 from 2021-10-11 14:23:47  <br>
/backup-demo/hello.txt  <br>
<br>
Found matching entries in snapshot f7d5b7c5 from 2021-10-11 14:12:39  <br>
/backup-demo/hello.txt<br>
</pre><br>
通过<code class="prettyprint">dump</code>命令可以查看指定快照指定文件的内容：<br>
<pre class="prettyprint"># restic dump f18cccc5 /backup-demo/hello2.txt  <br>
hello2<br>
</pre><br>
更强大的是可以通过<code class="prettyprint">mount</code>命令把整个快照内容挂载到本地：<br>
<pre class="prettyprint"># restic mount /mnt  <br>
Now serving the repository at /mnt  <br>
When finished, quit with Ctrl-c or umount the mountpoint.  <br>
# mount | grep /mnt  <br>
restic on /mnt type fuse (ro,nosuid,nodev,relatime,user_id=0,group_id=0)  <br>
# cat /mnt/snapshots/latest/backup-demo/hello2.txt  <br>
hello2  <br>
# umount /mnt<br>
</pre><br>
如上把所有快照挂载到本地的<code class="prettyprint">/mnt</code>目录下，并查看了<code class="prettyprint">latest</code>最新快照的<code class="prettyprint">hello2.txt</code>的内容，最后卸载<code class="prettyprint">/mnt</code>。<br>
<h4>数据恢复</h4>恢复文件也非常简单，直接使用<code class="prettyprint">restore</code>命令即可。<br>
<br>通过<code class="prettyprint">restore</code>命令可恢复指定快照的文件到本地：<br>
<pre class="prettyprint"># restic restore f18cccc5 -t /tmp/restore_data  <br>
restoring <Snapshot f18cccc5 of [/root/backup-demo] at 2021-10-11 14:40:36.459899498 +0800 CST by root@k8s-master-1> to /tmp/restore_data  <br>
# find /tmp/restore_data/  <br>
/tmp/restore_data/  <br>
/tmp/restore_data/backup-demo  <br>
/tmp/restore_data/backup-demo/new_file.txt  <br>
/tmp/restore_data/backup-demo/hello.txt  <br>
/tmp/restore_data/backup-demo/hello2.txt<br>
</pre><br>
当然也可以通过前面介绍的<code class="prettyprint">dump</code>命令实现单个文件恢复：<br>
<pre class="prettyprint">restic dump f18cccc5 /backup-demo/hello2.txt >hello2.txt<br>
</pre><br>
<h4>备份删除</h4>通过<code class="prettyprint">forget</code>可以删除指定<code class="prettyprint">id</code>的快照内容，当然我们实际使用更多的是按照时间或者快照数量进行快照保留或者删除，比如保留前7天的快照，保留最新的3个快照等等。<br>
<br>我们可以通过<code class="prettyprint">--dry-run</code>参数查看指定策略会删除的快照，但实际不会执行删除操作，用于检验参数是否符合预期。<br>
<br>如下我们执行只保留最新的3个快照：<br>
<pre class="prettyprint"># restic forget --keep-last=3 --dry-run  <br>
Applying Policy: keep 3 latest snapshots  <br>
keep 3 snapshots:  <br>
ID        Time                 Host                      Tags           Reasons        Paths  <br>
--------------------------------------------------------------------------------------------------------  <br>
7728a603  2021-10-11 14:23:47  int32bit-test-1                 last snapshot  /root/backup-demo  <br>
f18cccc5  2021-10-11 14:40:36  int32bit-test-1                 last snapshot  /root/backup-demo  <br>
56e7b24f  2021-10-11 15:37:50  int32bit-test-1  app_name=test  last snapshot  /root/backup-demo  <br>
--------------------------------------------------------------------------------------------------------  <br>
3 snapshots  <br>
<br>
remove 2 snapshots:  <br>
ID        Time                 Host                      Tags        Paths  <br>
--------------------------------------------------------------------------------------  <br>
55572d0c  2021-10-11 14:09:11  int32bit-test-1              /root/backup-demo  <br>
f7d5b7c5  2021-10-11 14:12:39  int32bit-test-1              /root/backup-demo  <br>
--------------------------------------------------------------------------------------  <br>
2 snapshots  <br>
<br>
keep 1 snapshots:  <br>
ID        Time                 Host                      Tags        Reasons        Paths  <br>
--------------------------------------------------------------------------------------------  <br>
112668f0  2021-10-11 15:28:22  int32bit-test-1              last snapshot  /recover  <br>
--------------------------------------------------------------------------------------------  <br>
1 snapshots  <br>
<br>
Would have removed the following snapshots:  <br>
&#123;55572d0c f7d5b7c5&#125; <br>
</pre><br>
其他删除策略，比如保留前2个小时的最新备份：<br>
<pre class="prettyprint"># restic  forget --dry-run --keep-hourly 2  <br>
Applying Policy: keep 2 hourly snapshots  <br>
keep 2 snapshots:  <br>
ID        Time                 Host                      Tags           Reasons          Paths  <br>
----------------------------------------------------------------------------------------------------------  <br>
56e7b24f  2021-10-11 15:37:50  int32bit-test-1  app_name=test  hourly snapshot  /root/backup-demo  <br>
f949e14b  2021-10-11 16:11:44  int32bit-test-1                 hourly snapshot  /root/backup-demo  <br>
----------------------------------------------------------------------------------------------------------  <br>
2 snapshots  <br>
<br>
remove 5 snapshots:  <br>
ID        Time                 Host                      Tags        Paths  <br>
--------------------------------------------------------------------------------------  <br>
55572d0c  2021-10-11 14:09:11  int32bit-test-1              /root/backup-demo  <br>
f7d5b7c5  2021-10-11 14:12:39  int32bit-test-1              /root/backup-demo  <br>
7728a603  2021-10-11 14:23:47  int32bit-test-1              /root/backup-demo  <br>
f18cccc5  2021-10-11 14:40:36  int32bit-test-1              /root/backup-demo  <br>
ab268923  2021-10-11 16:01:04  int32bit-test-1              /root/backup-demo  <br>
--------------------------------------------------------------------------------------  <br>
5 snapshots  <br>
<br>
Would have removed the following snapshots:  <br>
&#123;55572d0c 7728a603 ab268923 f18cccc5 f7d5b7c5&#125; <br>
</pre><br>
如上只保留前2个小时的备份，注意由于14点以及16点均备份了多次，该策略只会保留以小时为单位计算中最新的一份备份。<br>
<h4>备份计划</h4>restic为命令行CLI工具，不支持通过后台服务形式运行，因此不支持备份计划配置，但是很容易通过Linux自带的<code class="prettyprint">crontab</code>工具进行配置。<br>
<h3>使用开源Velero工具实现Kubernetes应用备份容灾</h3>前面介绍了restic工具以及提到了Velero工具，它是一个云原生的Kubernetes灾难恢复和迁移工具，<a href="https://velero.io/docs/v1.7/">Velero</a>的前身是Heptio公司的Ark工具，后被VMware公司收购，底层数据卷的备份用的正是restic。<br>
<br>Kubernetes备份工具除了Velero，其实还有已被veeam收购的kasten以及专门做PV卷备份的<a href="https://stash.run/">Stash</a>（底层用的也是restic）。<br>
<h4>Velero配置</h4>关于Velero的详细配置和安装方法可以参考官方文档，这里仅做简要描述。<br>
<br>以Minio对象存储为备份目标端为例，通过Velero客户端生成yaml文件：<br>
<pre class="prettyprint">./velero install \  <br>
--provider aws \  <br>
--plugins xxx/velero-plugin-for-aws:v1.0.0 \  <br>
--bucket velero \  <br>
--secret-file ./aws-iam-creds \  <br>
--backup-location-config region=test,s3Url=http://192.168.0.1,s3ForcePathStyle="true" \  <br>
--snapshot-location-config region=test \  <br>
--image xxx/velero:v1.6.3 \  <br>
--features=EnableCSI \  <br>
--use-restic \  <br>
--dry-run -o yaml<br>
</pre><br>
其中：<br>
<ul><li><code class="prettyprint">--plugins</code>以及<code class="prettyprint">--image</code>参数指定镜像仓库地址，仅当使用私有镜像仓库时需要配置。</li><li><code class="prettyprint">--use-restic</code>参数开启使用restic备份PV数据卷功能。</li><li>早期Kubernetes的volume卷不支持快照，因此备份PV卷时需要安装特定的后端存储卷插件，Kubernetes从v1.12开始CSI引入Snapshot后可以利用Snapshot特性实现备份，指定<code class="prettyprint">--features=EnableCSI</code>参数开启，开启该模式的底层存储必须支持snapshot，并且配置了snapshot相关的CRD以及<code class="prettyprint">volumesnapshotclass</code>（类似<code class="prettyprint">storageclass</code>）。</li></ul><br>
<br>数据恢复需要依赖velero-restic-restore-helper工具，如果使用私有镜像仓库，可以通过restic configmap配置私有镜像地址：<br>
<pre class="prettyprint">apiVersion: v1  <br>
kind: ConfigMap  <br>
metadata:  <br>
name: restic-config  <br>
namespace: velero  <br>
labels:  <br>
velero.io/plugin-config: ""  <br>
velero.io/restic: RestoreItemAction  <br>
data:  <br>
image: xxx/velero-restic-restore-helper:v1.6.3<br>
</pre><br>
<h4>通过Velero执行备份</h4>关于Velero的使用方法可以参考其他资料，这里仅以带PV的Nginx服务为例阐述备份过程以及恢复原理，Nginx的yaml声明文件内容如下：<br>
<pre class="prettyprint"># nginx-app-demo.yaml  <br>
---  <br>
apiVersion: v1  <br>
kind: Namespace  <br>
metadata:  <br>
name: nginx-app  <br>
---  <br>
apiVersion: v1  <br>
kind: PersistentVolumeClaim  <br>
metadata:  <br>
name: pvc-demo  <br>
namespace: nginx-app  <br>
spec:  <br>
accessModes:  <br>
- ReadWriteOnce  <br>
resources:  <br>
requests:  <br>
  storage: 1Gi  <br>
storageClassName: ceph-rbd-sata  <br>
---  <br>
apiVersion: apps/v1  <br>
kind: Deployment  <br>
metadata:  <br>
labels:  <br>
app: nginx  <br>
name: nginx  <br>
namespace: nginx-app  <br>
spec:  <br>
replicas: 1  <br>
selector:  <br>
matchLabels:  <br>
  app: nginx  <br>
template:  <br>
metadata:  <br>
  labels:  <br>
    app: nginx  <br>
  annotations:  <br>
    backup.velero.io/backup-volumes: mypvc  <br>
spec:  <br>
  containers:  <br>
  - image: nginx  <br>
    name: nginx  <br>
    volumeMounts:  <br>
      - name: mypvc  <br>
        mountPath: /usr/share/nginx/html  <br>
  volumes:  <br>
  - name: mypvc  <br>
    persistentVolumeClaim:  <br>
      claimName: pvc-demo  <br>
      readOnly: false  <br>
---  <br>
apiVersion: v1  <br>
kind: Service  <br>
metadata:  <br>
labels:  <br>
app: nginx  <br>
name: nginx  <br>
namespace: nginx-app  <br>
spec:  <br>
ports:  <br>
- port: 80  <br>
protocol: TCP  <br>
targetPort: 80  <br>
selector:  <br>
app: nginx<br>
</pre><br>
如上yaml仅需要关注如下两点：<br>
<ul><li>声明了一个PVC，并挂载到Nginx Pod的<code class="prettyprint">/usr/share/nginx/html</code>路径。</li><li>Pod添加了注解<code class="prettyprint">backup.velero.io/backup-volumes: mypvc</code>用于指定需要备份的Volume。因为并不是所有的Volume都必须备份，实际生产中可根据数据的重要性设置合理的备份策略，因此不建议开启<code class="prettyprint">--default-volumes-to-restic</code>选项，该选项会默认备份所有的Volume。</li></ul><br>
<br>我们进入Nginx中写入测试数据：<br>
<pre class="prettyprint"># kubectl  exec -t -i nginx-86f99c968-sj8ds -- /bin/bash  <br>
cd /usr/share/nginx/html/  <br>
echo "HelloWorld" >index.html  <br>
echo "hello1" >hello1.html  <br>
echo "hello2" >hello2.html<br>
</pre><br>
此时我们访问Nginx Service会输出<code class="prettyprint">HelloWorld</code>。<br>
<br>执行velero backup命令创建备份：<br>
<pre class="prettyprint">velero backup create nginx-backup-1 --include-namespaces nginx-app<br>
</pre><br>
查看备份信息：<br>
<pre class="prettyprint"># velero describe backups nginx-backup-1  <br>
Name:         nginx-backup-1  <br>
Namespace:    velero  <br>
Labels:       velero.io/storage-location=default  <br>
Phase:  Completed  <br>
Namespaces:  <br>
Included:  nginx-app  <br>
Storage Location:  default  <br>
Velero-Native Snapshot PVs:  auto  <br>
TTL:  720h0m0s  <br>
Backup Format Version:  1.1.0  <br>
Started:    2021-12-18 09:35:35 +0800 CST  <br>
Completed:  2021-12-18 09:35:47 +0800 CST  <br>
Expiration:  2022-01-17 09:35:35 +0800 CST  <br>
Total items to be backed up:  22  <br>
Items backed up:              22  <br>
Restic Backups :  <br>
Completed:  1<br>
</pre><br>
从描述信息中有如下几个值得关注的点：<br>
<ul><li>备份状态为Completed，说明备份完成，记录中会有备份开始时间和完成时间。</li><li>备份的资源数和完成数。</li><li>备份的Volume数（Restic Backups）。</li></ul><br>
<br><h4>备份数据管理以及迁移</h4>在S3中可以查看备份的内容：<br>
<pre class="prettyprint"># aws s3 ls velero/backups/nginx-backup-1/  <br>
2021-12-18 09:35:47         29 nginx-backup-1-csi-volumesnapshotcontents.json.gz  <br>
2021-12-18 09:35:47         29 nginx-backup-1-csi-volumesnapshots.json.gz  <br>
2021-12-18 09:35:47       4730 nginx-backup-1-logs.gz  <br>
2021-12-18 09:35:47        936 nginx-backup-1-podvolumebackups.json.gz  <br>
2021-12-18 09:35:47        372 nginx-backup-1-resource-list.json.gz  <br>
2021-12-18 09:35:47         29 nginx-backup-1-volumesnapshots.json.gz  <br>
2021-12-18 09:35:47      10391 nginx-backup-1.tar.gz  <br>
2021-12-18 09:35:47       2171 velero-backup.json<br>
</pre><br>
当然也可以通过download把备份下载导出到本地：<br>
<pre class="prettyprint"># velero backup download nginx-backup-1  <br>
Backup nginx-backup-1 has been successfully downloaded to /tmp/nginx-backup-1-data.tar.gz  <br>
# mkdir -p nginx-backup-1  <br>
# tar xvzf nginx-backup-1-data.tar.gz -C nginx-backup-1/  <br>
# ls -l nginx-backup-1/resources/  <br>
total 48  <br>
drwxr-xr-x 4 root root 4096 Dec 18 09:46 deployments.apps  <br>
drwxr-xr-x 4 root root 4096 Dec 18 09:46 endpoints  <br>
drwxr-xr-x 4 root root 4096 Dec 18 09:46 endpointslices.discovery.k8s.io  <br>
drwxr-xr-x 4 root root 4096 Dec 18 09:46 events  <br>
drwxr-xr-x 4 root root 4096 Dec 18 09:46 namespaces  <br>
drwxr-xr-x 4 root root 4096 Dec 18 09:46 persistentvolumeclaims  <br>
drwxr-xr-x 4 root root 4096 Dec 18 09:46 persistentvolumes  <br>
drwxr-xr-x 4 root root 4096 Dec 18 09:46 pods  <br>
drwxr-xr-x 4 root root 4096 Dec 18 09:46 replicasets.apps  <br>
drwxr-xr-x 4 root root 4096 Dec 18 09:46 secrets  <br>
drwxr-xr-x 4 root root 4096 Dec 18 09:46 serviceaccounts  <br>
drwxr-xr-x 4 root root 4096 Dec 18 09:46 services<br>
</pre><br>
如上两种方式都可以实现备份数据的导出迁移，但是需要注意的是，如上数据只包含Kubernetes声明资源的yaml文件，不包含最重要的Volume业务数据。这些数据保存在S3的<code class="prettyprint">velero/restic/nginx-app/</code>路径下，而这些数据是加密存储的。<br>
<br>从安全角度而言，这样做是安全合理的。但是对于运维人员来说，这是黑盒子，我们如何确定Volume的数据完整备份了呢（Verifiable原则）。或者极端场景下，我的业务不跑容器了，想迁到物理机上本地直接运行，我的业务数据如何高效快速迁移。<br>
<br>办法总是有的，通过Velero恢复到容器中，然后通过容器把数据迁走就可以了，但是这似乎有点麻烦，而且依赖于Velero。有没有办法直接通过restic工具进行备份数据的管理呢？<br>
<br>根据前面关于restic的介绍，这些数据是加密存储的，那我们读取数据就需要restic的仓库密码。<br>
<br>这个密码其实存储在<code class="prettyprint">velero-restic-credentials</code>  Secret中，任何有权限的管理员都可以读取，因此这里也特别需要注意控制velero的访问权限。<br>
<pre class="prettyprint"># kubectl get secrets velero-restic-credentials \  <br>
-o jsonpath='&#123;.data.repository-password&#125;' | base64 -d<br>
</pre><br>
拿到了仓库密码，我们就能使用原生的restic工具对备份数据进行管理了。<br>
<br>首先查看snapshots列表：<br>
<pre class="prettyprint"># restic -r s3:http://192.168.0.1/velero/restic/nginx-app snapshots  <br>
14fc2081  2021-12-18 09:35:45 ... # 输出有点长，省去了后面的输出内容<br>
</pre><br>
查看备份的文件：<br>
<pre class="prettyprint"># restic -r s3:http://192.168.0.1/velero/restic/nginx-app ls 14fc2081  <br>
snapshot 14fc2081:  <br>
/hello1.html  <br>
/hello2.html  <br>
/index.html<br>
</pre><br>
查看指定备份文件的内容：<br>
<pre class="prettyprint"># restic -r s3:http://192.168.0.1/velero/restic/nginx-app dump 14fc2081 /hello2.html  <br>
hello2<br>
</pre><br>
通过restic工具，我们可以很轻易的进行备份数据管理以及数据迁移。<br>
<h4>数据恢复</h4>前面我们通过Velero备份了nginx-app namespace下的所有资源包括Volume数据。<br>
<br>现在我们把整个nginx-app删除：<br>
<pre class="prettyprint">kubectl delete -f nginx-app-demo.yaml<br>
</pre><br>
该命令会把整个namespace的所有资源彻底删除，包括PV数据卷的文件，在底层存储中也会彻底把Volume删除。<br>
<pre class="prettyprint"># kubectl get all -n nginx-app  <br>
No resources found in nginx-app namespace.  <br>
# kubectl get ns nginx-app  <br>
Error from server (NotFound): namespaces "nginx-app" not found<br>
</pre><br>
从如上输出结果看，数据已经完全删除。<br>
<br>接着我们通过Velero执行数据恢复：<br>
<pre class="prettyprint"># velero restore create --from-backup nginx-backup-1   <br>
Restore request "nginx-backup-1-20211218102506" submitted successfully.  <br>
# velero restore get  <br>
NAME                            BACKUP           STATUS  <br>
nginx-backup-1-20211218102506   nginx-backup-1   InProgress  <br>
# velero restore get  <br>
NAME                            BACKUP           STATUS  <br>
nginx-backup-1-20211218102506   nginx-backup-1   Completed<br>
</pre><br>
velero恢复完成后，我们验证nginx应用是否完全恢复，首先查看Pod和Service：<br>
<pre class="prettyprint"># kubectl get pod -n nginx-app  <br>
NAME                    READY   STATUS    RESTARTS   AGE  <br>
nginx-86f99c968-8zh6m   1/1     Running   0          103s  <br>
# kubectl get svc -n nginx-app  <br>
NAME    TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE  <br>
nginx   ClusterIP   10.106.140.195   <none>        80/TCP    2m37<br>
</pre><br>
从输出结果看，原来nginx-app namespace的资源均完全恢复并且处于运行状态。接下来只需要检查业务数据是否恢复：<br>
<pre class="prettyprint"># kubectl exec -t -i -n nginx-app nginx-86f99c968-8zh6m -- ls /usr/share/nginx/html/  <br>
hello1.html  hello2.html  index.html  lost+found  <br>
# kubectl get svc -n nginx-app  <br>
NAME    TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE  <br>
nginx   ClusterIP   10.106.140.195   <none>        80/TCP    2m37s  <br>
# curl  10.106.140.195  <br>
HelloWorld<br>
</pre><br>
经验证，业务数据是OK的，业务也正常恢复。<br>
<br>我们查看Pod声明：<br>
<pre class="prettyprint">apiVersion: v1  <br>
kind: Pod  <br>
metadata:  <br>
annotations:  <br>
backup.velero.io/backup-volumes: mypvc  <br>
labels:  <br>
app: nginx  <br>
pod-template-hash: 86f99c968  <br>
velero.io/backup-name: nginx-backup-1  <br>
velero.io/restore-name: nginx-backup-1-20211218102506  <br>
name: nginx-86f99c968-8zh6m  <br>
namespace: nginx-app  <br>
spec:  <br>
containers:  <br>
- image: nginx  <br>
name: nginx  <br>
volumeMounts:  <br>
- mountPath: /usr/share/nginx/html  <br>
  name: mypvc  <br>
initContainers:  <br>
- args:  <br>
- ead72033-f495-4223-9358-6f97c920e9ae  <br>
command:  <br>
- /velero-restic-restore-helper  <br>
env:  <br>
- name: POD_NAMESPACE  <br>
  valueFrom:  <br>
    fieldRef:  <br>
      apiVersion: v1  <br>
      fieldPath: metadata.namespace  <br>
- name: POD_NAME  <br>
  valueFrom:  <br>
    fieldRef:  <br>
      apiVersion: v1  <br>
      fieldPath: metadata.name  <br>
image: velero-restic-restore-helper:v1.6.3  <br>
imagePullPolicy: IfNotPresent  <br>
name: restic-wait  <br>
volumeMounts:  <br>
- mountPath: /restores/mypvc  <br>
  name: mypvc  <br>
volumes:  <br>
- name: mypvc  <br>
persistentVolumeClaim:  <br>
  claimName: rbd-pvc-demo<br>
</pre><br>
yaml文件与之前初始化声明的大体一样，仅需留意如下两点：<br>
<ul><li>Pod增加Velero备份和恢复相关label。</li><li>嵌入了一个<code class="prettyprint">initContainer</code>，通过<code class="prettyprint">velero-restic-restore-helper</code>实现volume数据的恢复，该工具其实就是restic命令的包装。</li></ul><br>
<br><h4>备份策略与计划</h4>前面提到restic本身是一个命令行CLI工具，不支持备份计划任务。但是velero是支持备份计划的，备份计划支持如下配置：<br>
<ul><li>备份时间，crontab语法。</li><li>备份保留时间，通过ttl指定，默认30天。</li><li>备份内容，支持指定namespace或者基于label指定具体的备份资源。</li></ul><br>
<br>关于Velero备份计划的管理，这里不详细介绍，感兴趣的读者可以参考官方文档，也通过<code class="prettyprint">velero create schedule -h</code>命令查看帮助文档和样例：<br>
<pre class="prettyprint"># Create a backup every 6 hours.  <br>
velero create schedule NAME --schedule="0 */6 * * *"  <br>
<br>
# Create a backup every 6 hours with the @every notation.  <br>
velero create schedule NAME --schedule="@every 6h"  <br>
<br>
# Create a daily backup of the web namespace.  <br>
velero create schedule NAME --schedule="@every 24h" --include-namespaces web  <br>
<br>
# Create a weekly backup, each living for 90 days (2160 hours).  <br>
velero create schedule NAME --schedule="@every 168h" --ttl 2160h0m0s<br>
</pre><br>
<h4>Kubernetes企业备份容灾方案</h4>根据前面的介绍，可设计Kubernetes的粗略版备份容灾方案：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211218/6d0b23349b467ea22b61f09b602ea20e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211218/6d0b23349b467ea22b61f09b602ea20e.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Kubernetes备份容灾方案</em><br>
<br>其中：<br>
<ul><li>minio为开源的对象存储，为velero/restic提供备份存储后端，实际生产时调整为企业对象存储系统。</li><li>远端存储为异地存储系统，比如异地磁带库、NBU，或者跨region的异地对象存储系统。</li></ul><br>
<br>备份流程：<br>
<ol><li>Kubernetes的所有资源包括Pod、Deployment、ConfigMap、Secret、PV卷数据等通过Velero备份到对象存储。</li><li>通过minio-sync实现实时同步数据到远端同城异地存储系统。</li></ol><br>
<br>恢复流程：<br>
<br><strong>场景一：集群状态无异常，人为误操作导致数据被删。</strong><br>
<br>直接通过Velero恢复指定时间的数据进行恢复即可。<br>
<br><strong>场景二：PV底层的存储系统crash导致数据丢失。</strong><br>
<br>恢复存储系统集群或者极端情况下重搭存储集群，然后使用Velero从对象存储中恢复数据。<br>
<br><strong>场景三：极端场景下，整个数据中心或者region crash导致数据丢失。</strong><br>
<br>重建环境，业务数据需要从异地数据中复制到本地，然后借助velero从新建对象存储中进行数据恢复。<br>
<br><strong>场景四：Kubernetes环境迁移。</strong><br>
<br>新建Kubernetes集群，通过Velero指定备份点迁移数据到新环境中。<br>
<br><strong>场景五：业务从Kubernetes运行迁移到虚拟机或者物理机运行。</strong><br>
<br>通过Restic从对象存储中把业务数据导出到虚拟机的数据卷中即可。<br>
<h3>Kubernetes集群备份</h3>前面介绍了Kubernetes应用级别的备份方案，除了上层应用级别备份，集群本身的备份也尤为重要，Kubernetes几乎所有的元数据均存储在etcd中，因此集群备份的核心就是etcd的备份，除此之外Kubernetes的证书、kubeadm的配置等也需要在备份策略中考虑到，在集群恢复中不可或缺。<br>
<br>关于Kubernetes证书、kubeadm配置的备份可以直接使用前面介绍的restic工具对整个<code class="prettyprint">/etc/kubernetes</code>目录进行备份，而etcd的备份官方也有<a href="https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/#backing-up-an-etcd-cluster">介绍backing-up-an-etcd-cluster</a>。<br>
<pre class="prettyprint">ETCDCTL_API=3 etcdctl --endpoints $ENDPOINT snapshot save snapshotdb<br>
</pre><br>
比如备份etcd到Minio对象存储中，参考脚本如下：<br>
<pre class="prettyprint">#!/bin/sh  <br>
# bootstrap.sh  <br>
export ETCDCTL_API=3  <br>
<br>
MASTER_ENDPOINT=$(etcdctl --endpoints=$ETCD_ENDPOINTS \  <br>
--cacert=/etc/ssl/etcd/ca.crt \  <br>
--cert=/etc/ssl/etcd/etcd.crt \  <br>
--key=/etc/ssl/etcd/etcd.key \  <br>
endpoint status \  <br>
| awk -F ',' '&#123;printf("%s %s\n", $1,$5)&#125;' \  <br>
| tr -s ' ' |  awk '/true/&#123;print $1&#125;')  <br>
<br>
echo "etcd master endpoint is $&#123;MASTER_ENDPOINT&#125;"  <br>
<br>
BACKUP_FILE=etcd-backup-$(date +%Y%m%d%H%M%S).db  <br>
<br>
etcdctl --endpoints=$MASTER_ENDPOINT \  <br>
--cacert=/etc/ssl/etcd/ca.crt \  <br>
--cert=/etc/ssl/etcd/etcd.crt \  <br>
--key=/etc/ssl/etcd/etcd.key \  <br>
snapshot save $BACKUP_FILE  <br>
<br>
aws --endpoint $S3_ENDPOINT s3 cp $BACKUP_FILE s3://$BUCKET_NAME  <br>
<br>
for f in $(aws --endpoint $S3_ENDPOINT \  <br>
s3 ls $BUCKET_NAME | head -n "-$&#123;KEEP_LAST_BACKUP_COUNT&#125;" \  <br>
| awk '&#123;print $4&#125;'); do  <br>
aws --endpoint $S3_ENDPOINT s3 rm s3://$BUCKET_NAME/$f  <br>
done<br>
</pre><br>
如上脚本首先获取Master节点的endpoint，然后通过master endpoint创建etcd快照。快照生成后通过AWS S3命令拷贝到远端对象存储中，最后会删除一些老的备份，只保留指定数量的备份数量。<br>
<br>可以把如上脚本<code class="prettyprint">bootstrap.sh</code>做成Docker镜像：<br>
<pre class="prettyprint">FROM python:alpine  <br>
ARG ETCD_VERSION=v3.4.3  <br>
RUN apk add --update --no-cache ca-certificates tzdata openssl  <br>
RUN wget https://github.com/etcd-io/etcd/releases/download/$&#123;ETCD_VERSION&#125;/etcd-$&#123;ETCD_VERSION&#125;-linux-amd64.tar.gz \  <br>
&& tar xzf etcd-$&#123;ETCD_VERSION&#125;-linux-amd64.tar.gz \  <br>
&& mv etcd-$&#123;ETCD_VERSION&#125;-linux-amd64/etcdctl /usr/local/bin/etcdctl \  <br>
&& rm -rf etcd-$&#123;ETCD_VERSION&#125;-linux-amd64*  <br>
RUN pip3 install awscli  <br>
ENV ETCDCTL_API=3  <br>
ADD bootstrap.sh /  <br>
RUN chmod +x /bootstrap.sh  <br>
CMD ["/bootstrap.sh"] <br>
</pre><br>
把etcd的证书以及Minio的AKSK存储到Kubernetes Secret中：<br>
<pre class="prettyprint">#!/bin/bash  <br>
kubectl create secret generic etcd-tls -o yaml \  <br>
--from-file /etc/kubernetes/pki/etcd/ca.crt \  <br>
--from-file /etc/kubernetes/pki/etcd/server.crt \  <br>
--from-file /etc/kubernetes/pki/etcd/server.key \  <br>
| sed 's/server/etcd/g'  <br>
kubectl create secret generic s3-credentials \  <br>
-o yaml --from-file ~/.aws/credentials<br>
</pre><br>
通过Kubernetes自带内置的CronJob实现定时备份：<br>
<pre class="prettyprint">apiVersion: batch/v1beta1  <br>
kind: CronJob  <br>
metadata:  <br>
name: etcd-backup  <br>
namespace: etcd-backup  <br>
spec:  <br>
jobTemplate:  <br>
metadata:  <br>
  name: etcd-backup  <br>
spec:  <br>
  template:  <br>
    spec:  <br>
      containers:  <br>
      - image: etcd-backup:v3.4.3  <br>
        imagePullPolicy: IfNotPresent  <br>
        name: etcd-backup  <br>
        volumeMounts:  <br>
        - name: s3-credentials  <br>
          mountPath: /root/.aws  <br>
        - name: etcd-tls  <br>
          mountPath: /etc/ssl/etcd  <br>
        - name: localtime  <br>
          mountPath: /etc/localtime  <br>
          readOnly: true  <br>
        env:  <br>
        - name: ETCD_ENDPOINTS  <br>
          value: "192.168.1.1:2379,192.168.1.2:2379,192.168.1.3:2379"  <br>
        - name: BUCKET_NAME  <br>
          value: etcd-backup  <br>
        - name: S3_ENDPOINT  <br>
          value: "http://192.168.1.53"  <br>
        - name: KEEP_LAST_BACKUP_COUNT  <br>
          value: "7"  <br>
      volumes:  <br>
      - name: s3-credentials  <br>
        secret:  <br>
          secretName: s3-credentials  <br>
      - name: etcd-tls  <br>
        secret:  <br>
          secretName: etcd-tls  <br>
      - name: localtime  <br>
        hostPath:  <br>
          path: /etc/localtime  <br>
      restartPolicy: OnFailure  <br>
schedule: '0 0 * * *'  <br>
</pre><br>
如上CronJob配置每天0点对etcd进行备份到Minio对象存储中。<br>
<h3>总结</h3>本文首先介绍了Kubernetes备份的思路以及开源restic工具。然后介绍了使用开源Velero工具实现Kubernetes应用级别备份容灾方案，重点介绍了PV卷业务数据的备份和恢复过程。最后介绍了通过etcd备份实现Kubernetes集群级别的备份容灾。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/nHkXzzAR8Rilf-eRSTJxoQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/nHkXzzAR8Rilf-eRSTJxoQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            