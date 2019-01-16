1、AttributeError: 'module' object has noattribute 'random_crop'

将tf.scalar_summary(loss.op.name,loss)

改为tf.summary.scalar(loss.op.name, loss)即可

2、AttributeError: 'module' object has no attribute'per_image_whitening'

将float_image = tf.image.per_image_whitening(distorted_image)

改为float_image = tf.image.per_image_standardization(distorted_image)

3、AttributeError: module 'tensorflow' has no attribute 'image_summary'

将tf.image_aummary('images', images)改为


tf.summary.image('images', images)

4、AttributeError: module 'tensorflow' has no attribute 'histogram_summary'

改为tf.summary.histogram(tensor_name + '/activations', x)

5、AttributeError: module 'tensorflow' has no attribute 'scalar_summary'

改为tf.summary.scalar(tensor_name + '/sparsity', tf.nn.zero_fraction(x))

6、AttributeError: module 'tensorflow' has no attribute 'mul'

改为weight_decay = tf.multiply(tf.nn.l2_loss(var), wd, name='weight_loss')

7、ValueError: Shapes (2, 128, 1) and () are incompatible

改为concated = tf.concat([indices, sparse_labels],1)

8、ValueError: Only call `softmax_cross_entropy_with_logits` with named arguments (labels=..., logits=..., ...)

改为cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=dense_labels, name='cross_entropy_per_example')

9、TypeError: Using a `tf.Tensor` as a Python `bool` is not allowed. Use `if t is not None:` instead of `if t:` to test if a tensor is defined, and use TensorFlow ops such as tf.cond to execute subgraphs conditioned on the value of a tensor.

if grad: 改为  if grad is not None:

10、AttributeError: module 'tensorflow' has no attribute 'merge_all_summaries'

改为summary_op = tf.summary.merge_all()

11、AttributeError: module 'tensorflow.python.training.training' has no attribute 'SummaryWriter'

改为summary_writer = tf.summary.FileWriter(FLAGS.train_dir,graph_def=sess.graph_def)


