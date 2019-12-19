import argparse
from repository import GithubRepository

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Set github status')
    parser.add_argument('--repo', required=True, help="user/repo")
    parser.add_argument('--sha', required=True)

    def status_type(status):
        if status in ('pending', 'success', 'error', 'failure'):
            return status
        raise ValueError()

    parser.add_argument('--token', help="Token")
    parser.add_argument('--desc', help="Description")
    parser.add_argument('--url', help="Job url")
    parser.add_argument('--status', type=status_type, required=True)

    args = parser.parse_args()

    ghr = GithubRepository(args.repo, args.token)
    ghr.update_status(args.sha, args.status, args.desc, args.url)
