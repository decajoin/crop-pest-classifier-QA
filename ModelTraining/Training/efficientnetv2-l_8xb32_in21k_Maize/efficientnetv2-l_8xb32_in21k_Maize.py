auto_scale_lr = dict(base_batch_size=64)
data_preprocessor = dict(
    mean=[
        115.3113,
        133.2982,
        88.8901,
    ],
    num_classes=7,
    std=[
        52.6689,
        54.4978,
        53.0697,
    ],
    to_rgb=True)
dataset_type = 'CustomDataset'
default_hooks = dict(
    checkpoint=dict(interval=1, type='CheckpointHook'),
    logger=dict(interval=100, type='LoggerHook'),
    param_scheduler=dict(type='ParamSchedulerHook'),
    sampler_seed=dict(type='DistSamplerSeedHook'),
    timer=dict(type='IterTimerHook'),
    visualization=dict(enable=False, type='VisualizationHook'))
default_scope = 'mmpretrain'
env_cfg = dict(
    cudnn_benchmark=False,
    dist_cfg=dict(backend='nccl'),
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0))
launcher = 'none'
load_from = None
log_level = 'INFO'
model = dict(
    backbone=dict(arch='l', type='EfficientNetV2'),
    head=dict(
        in_channels=1280,
        loss=dict(loss_weight=1.0, type='CrossEntropyLoss'),
        num_classes=7,
        topk=(
            1,
            5,
        ),
        type='LinearClsHead'),
    neck=dict(type='GlobalAveragePooling'),
    type='ImageClassifier')
optim_wrapper = dict(
    clip_grad=dict(max_norm=5.0),
    optimizer=dict(lr=0.004, momentum=0.9, type='SGD', weight_decay=0.0001))
param_scheduler = dict(
    by_epoch=True, gamma=0.1, milestones=[
        30,
        60,
        90,
    ], type='MultiStepLR')
randomness = dict(deterministic=False, seed=None)
resume = False
test_cfg = dict()
test_dataloader = dict(
    batch_size=32,
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        data_root='data/Maize/test',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(crop_padding=0, crop_size=224, type='EfficientNetCenterCrop'),
            dict(type='PackInputs'),
        ],
        type='CustomDataset'),
    num_workers=5,
    persistent_workers=True,
    pin_memory=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
test_evaluator = dict(
    topk=(
        1,
        5,
    ), type='Accuracy')
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(crop_padding=0, crop_size=224, type='EfficientNetCenterCrop'),
    dict(type='PackInputs'),
]
train_cfg = dict(by_epoch=True, max_epochs=100, val_interval=1)
train_dataloader = dict(
    batch_size=32,
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        data_root='data/Maize/train',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(scale=224, type='EfficientNetRandomCrop'),
            dict(direction='horizontal', prob=0.5, type='RandomFlip'),
            dict(type='PackInputs'),
        ],
        type='CustomDataset'),
    num_workers=5,
    persistent_workers=True,
    pin_memory=True,
    sampler=dict(shuffle=True, type='DefaultSampler'))
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(scale=224, type='EfficientNetRandomCrop'),
    dict(direction='horizontal', prob=0.5, type='RandomFlip'),
    dict(type='PackInputs'),
]
val_cfg = dict()
val_dataloader = dict(
    batch_size=32,
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        data_root='data/Maize/val',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(crop_padding=0, crop_size=224, type='EfficientNetCenterCrop'),
            dict(type='PackInputs'),
        ],
        type='CustomDataset'),
    num_workers=5,
    persistent_workers=True,
    pin_memory=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
val_evaluator = dict(
    topk=(
        1,
        5,
    ), type='Accuracy')
vis_backends = [
    dict(type='LocalVisBackend'),
]
visualizer = dict(
    type='UniversalVisualizer', vis_backends=[
        dict(type='LocalVisBackend'),
    ])
work_dir = './work_dirs/efficientnetv2-l_8xb32_in21k_Maize'
