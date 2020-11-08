import argparse

def build_flags():
    parser = argparse.ArgumentParser('')
    parser.add_argument('--working_dir', required=True)
    parser.add_argument('--gpu', action='store_true')
    parser.add_argument('--seed', type=int, default=1)
    parser.add_argument('--mode', choices=['train', 'eval', 'eval_fixedwindow'], required=True)
    parser.add_argument('--load_model')
    parser.add_argument('--load_best_model', action='store_true')
    parser.add_argument('--continue_training', action='store_true')
    parser.add_argument('--model_type', choices=['nri', 'dnri'])

    # Training Params
    parser.add_argument('--num_epochs', type=int)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--mom', type=float, default=0)
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--sub_batch_size', type=int)
    parser.add_argument('--val_batch_size', type=int)
    parser.add_argument('--val_interval', type=int, default=5)
    parser.add_argument('--test', action='store_true')
    parser.add_argument('--use_adam', action='store_true')
    parser.add_argument('--lr_decay_factor', type=float)
    parser.add_argument('--lr_decay_steps', type=int)
    parser.add_argument('--clip_grad_norm', type=float)
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--tune_on_nll', action='store_true')
    parser.add_argument('--val_teacher_forcing', action='store_true')
    parser.add_argument('--accumulate_steps', type=int, default=-1)
    parser.add_argument('--max_burn_in_count', type=int, default=-1)
    
    # Model Params
    parser.add_argument('--no_prior', action='store_true')
    parser.add_argument('--avg_prior', action='store_true')
    parser.add_argument('--prior_num_layers', type=int, default=1)
    parser.add_argument('--prior_hidden_size', type=int, default=256)
    parser.add_argument('--use_learned_prior', action='store_true')
    parser.add_argument('--graph_type', choices=['static', 'dynamic'], required=True)
    parser.add_argument('--avg_encoder_inputs', action='store_true')
    parser.add_argument('--use_dynamic_graph', action='store_true')
    parser.add_argument('--use_static_encoder', action='store_true')
    parser.add_argument('--encoder_rnn_type', choices=['lstm', 'gru'], default='lstm')
    parser.add_argument('--decoder_rnn_type', choices=['lstm', 'gru'], default='gru')
    parser.add_argument('--encoder_hidden', type=int, default=256)
    parser.add_argument('--encoder_rnn_hidden', type=int)
    parser.add_argument('--num_edge_types', type=int, default=2)
    parser.add_argument('--encoder_dropout', type=float, default=0.0)
    parser.add_argument('--encoder_unidirectional', action='store_true')
    parser.add_argument('--encoder_bidirectional', action='store_true')
    parser.add_argument('--encoder_no_factor', action='store_true', default=False)
    parser.add_argument('--decoder_hidden', type=int, default=256)
    parser.add_argument('--decoder_msg_hidden', type=int, default=256)
    parser.add_argument('--decoder_dropout', type=float, default=0.0)
    parser.add_argument('--skip_first', action='store_true', default=False)
    parser.add_argument('--uniform_prior', action='store_true')
    parser.add_argument('--no_edge_prior', type=float)
    parser.add_argument('--teacher_forcing_steps', type=int, default=10)
    parser.add_argument('--gumbel_temp', type=float, default=0.5)
    parser.add_argument('--train_hard_sample', action='store_true')
    parser.add_argument('--normalize_kl', action='store_true')
    parser.add_argument('--normalize_kl_per_var', action='store_true')
    parser.add_argument('--normalize_nll', action='store_true')
    parser.add_argument('--normalize_nll_per_var', action='store_true')
    parser.add_argument('--kl_coef', type=float, default=1.)
    parser.add_argument('--no_encoder_bn', action='store_true')
    parser.add_argument('--encoder_mlp_hidden', type=int, default=256)
    parser.add_argument('--encoder_mlp_num_layers', type=int, default=1)
    parser.add_argument('--rnn_hidden', type=int, default=64)
    parser.add_argument('--teacher_forcing_prior', action='store_true')
    parser.add_argument('--decoder_rnn_hidden', type=int)
    parser.add_argument('--encoder_save_eval_memory', action='store_true')
    parser.add_argument('--encoder_normalize_mode', choices=[None, 'normalize_inp', 'normalize_all'])
    parser.add_argument('--normalize_inputs', action='store_true')
    #Modes
    return parser